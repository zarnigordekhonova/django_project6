from django.urls import path
from app1.views import country, date


urlpatterns = [
    path('country', country),
    path('date', date)
]