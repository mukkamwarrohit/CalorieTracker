from django.shortcuts import render, redirect
from .models import CalorieEntry
from .forms import CalorieEntryForm
from django.db.models import Sum

def home(request):
    # Process form submission
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalorieEntryForm()

    # Retrieve past entries and calculate total calories
    entries = CalorieEntry.objects.all().order_by('-date')
    total_calories = CalorieEntry.objects.aggregate(Sum('calories'))['calories__sum'] or 0

    context = {
        'form': form,
        'entries': entries,
        'total_calories': total_calories,
    }
    return render(request, 'tracker/home.html', context)
