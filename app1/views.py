from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def country(request):
    return HttpResponse('<h1>where do you want to go--> Japan <h1><hr/>')


def date(request):
    return HttpResponse('<h1>on which day--> dd/mm/yyyy<h1><hr/>')