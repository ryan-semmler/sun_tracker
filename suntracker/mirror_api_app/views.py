from django.shortcuts import render
from django.http import HttpResponse


def api(request, height, distance, year, month, day, latitude, longitude, direction):

    # tests regex variable extraction from url
    return HttpResponse("<br>".join(['height: {}'.format(height),
                                     'distance: {}'.format(distance),
                                     'year: {}'.format(year),
                                     'month: {}'.format(month),
                                     'day: {}'.format(day),
                                     'latitude: {}'.format(latitude),
                                     'longitude: {}'.format(longitude),
                                     'direction: {}'.format(direction)]
                                    ))
