import requests
from django.http import JsonResponse
from django.conf import settings

def get_weather(request):
    city = request.GET.get("city", "Prague")  # Город по умолчанию - Прага
    api_key = settings.OPENWEATHER_API_KEY    # Ключ API из настроек
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({"error": "Could not fetch weather data"}, status=400)
    


