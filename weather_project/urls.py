from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),              # Админка
    path('api/', include('weather_app.urls')),     # Подключаем маршруты из weather_app
]