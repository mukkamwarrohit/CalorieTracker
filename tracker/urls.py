from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Base URL for the tracker app
]
