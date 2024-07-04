from django.http import JsonResponse
import requests

def GetWeather(request):
    apiKey = 'ea52c1dfdd8993a2ea8d63e03a3f159c';

    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apiKey}&units=metric"
    
    response = requests.get(url).json()

    return JsonResponse(response)