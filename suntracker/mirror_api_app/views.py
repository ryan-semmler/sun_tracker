# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from .web_scrape import get_dict
from .mirror_angle import main
from json import dumps
# import requests
# from time import time
from .forms import MainOptions


def api(request, height, distance, year, month, day, lat, lon, direction):

    return HttpResponse(dumps(main(height, distance, year, month,
                                   day, lat, lon, direction)))


def options(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MainOptions(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MainOptions()

    return render(request, 'options.html', {'form': form})


def get_data(request, **kwargs):
    return render(request, 'get_data.html', {'kwargs': kwargs,
                                             'locals': locals()})
