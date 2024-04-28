from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def ticket_price(request):
    return HttpResponse('<h1>Price--> $460 <h1><hr/>')


def which_class(request):
    return HttpResponse('<h1>Whcih class--> Econom <h1><hr/>')