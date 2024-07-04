from django.urls import path
from . import views

urlpatterns = [
    path('weather/',views.GetWeather,name='weather')
]