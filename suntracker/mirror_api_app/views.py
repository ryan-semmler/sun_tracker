# from django.shortcuts import render
from django.http import HttpResponse
# from .web_scrape import get_dict
from .mirror_angle import main
from json import dumps
# import requests
# from time import time


def api(request, height, distance, year, month, day, lat, lon, direction):

    return HttpResponse(dumps(main(height, distance, year, month, day, lat, lon, direction)))

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
