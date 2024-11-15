from django.db import models
from django.utils import timezone

class CalorieEntry(models.Model):
    date = models.DateField(default=timezone.now)
    food_item = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.food_item} - {self.calories} kcal"
