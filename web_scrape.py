# import csv
# import urllib.request
import requests
# from lxml import html
# from datetime import time


def get_dict(info):
    """
    Takes dict 'info' for date and location to return dict of sun altitude and
    azimuth for every minute of daylight at that date.
    """

    # https://midcdmz.nrel.gov/apps/solpos.pl?syear=2005&smonth=1&sday=17&eyear=2005&emonth=1&eday=17&step=1&stepunit=1&latitude=1.111&longitude=2.222&timezone=3.333&press=4.444&temp=5.555&aspect=6.666&tilt=7.777&solcon=8.888&sbwid=9.999&sbrad=12&sbsky=.34&interval=56&field=34&field=2&zip=0
    smonth = info['start_month']
    sday = info['start_day']
    syear = info['start_year']
    lat = info['latitude']
    lon = info['longitude']

    url = ''.join(['https://midcdmz.nrel.gov/apps/solpos.pl?',
                   'syear={}'.format(syear),
                   '&smonth={}'.format(smonth),
                   '&sday={}'.format(sday),
                   '&eyear={}'.format(syear),
                   '&emonth={}'.format(smonth),
                   '&eday={}'.format(sday),
                   '&step=1&stepunit=1&latitude={}'.format(lat),
                   '&longitude={}'.format(lon),
                   '&timezone=-5&press=1030&temp=23&aspect=180&tilt=0',
                   '&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04',
                   '&interval=0&field=34&field=2&zip=0'])

    page = requests.get(url)
    # tree = html.fromstring(page.content)
    total_string = ""
    for item in page:
        total_string += str(item)[1:]
    clean_string = ''.join(total_string.split("''"))
    all_data = clean_string.split('\\n')[1:-1]
    data = {}
    for row in all_data:
        split_data = row.split(',')
        if float(split_data[2]) < 90:
            altitude = round(90 - float(split_data[2]), 4)
            data[split_data[1]] = {'altitude': altitude,
                                   'azimuth': float(split_data[3])}
    return data
