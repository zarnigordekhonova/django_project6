from django.urls import path
from app2.views import ticket_price, which_class


urlpatterns = [
    path('price', ticket_price),
    path('class', which_class)
]