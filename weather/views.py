from django.http import JsonResponse
from django.core.cache import cache
import requests

def get_region_key(lat,lon,precision=1):
    """
    Round the latitude and longitude which helps in grouping nearby locations together
    """
    return f"{round(float(lat),precision)}_{round(float(lon),precision)}"

def GetWeather(request):
    apiKey = 'ea52c1dfdd8993a2ea8d63e03a3f159c';

    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')

    region_key = get_region_key(latitude,longitude,precision=1)

    #cache related 
    cache_key = f"weather_{region_key}"
    cache_time = 3600

    #check in cache 
    response = cache.get(cache_key)

    if not response:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apiKey}&units=metric"
    
        response = requests.get(url).json()
        cache.set(cache_key,response,cache_time)

    return JsonResponse(response)