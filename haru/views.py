from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sumimasen_desuka(request):
    return HttpResponse("<h1>Arigato, Thomas-san</h1>")