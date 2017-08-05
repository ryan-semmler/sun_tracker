# from django.shortcuts import render
from django.http import HttpResponse
from .web_scrape import get_dict
# import requests
# from time import time


def api(request, height, distance, year, month, day, lat, lon, direction):

    return HttpResponse(get_dict(year, month, day, lat, lon))

    # # tests regex variable extraction from url
    # return HttpResponse("<br>".join(['height: {}'.format(height),
    #                                  'distance: {}'.format(distance),
    #                                  'year: {}'.format(year),
    #                                  'month: {}'.format(month),
    #                                  'day: {}'.format(day),
    #                                  'latitude: {}'.format(latitude),
    #                                  'longitude: {}'.format(longitude),
    #                                  'direction: {}'.format(direction)]
    #                                 ))


def options():
    pass
