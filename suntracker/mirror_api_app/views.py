from django.shortcuts import render
from django.http import HttpResponse


def api(request, height, distance, year, month, day, latitude, longitude, direction):
    
