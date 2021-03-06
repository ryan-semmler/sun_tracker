import requests
from time import time
from pprint import pformat


def get_timezone(lat, lon, year, month, day):
    """
    returns time difference, in hours, from utc.
    """

    api_key = 'AIzaSyDDbyw4tB8C9LhZ80VLnYFsLeBqBrXEj9g'
    timestamp = time()
    url = ''.join(['https://maps.googleapis.com/maps/api/timezone/json?',
                   'location={},{}'.format(lat, lon),
                   '&timestamp={}'.format(timestamp),
                   '&key={}'.format(api_key)])
    response = requests.get(url).json()
    offset = (response['dstOffset'] + response['rawOffset']) / 3600
    return offset


def get_dict(year, month, day, lat, lon):
    """
    Takes dict 'info' for date and location to return dict of sun altitude and
    azimuth for every minute of daylight at that date.
    """

    # https://midcdmz.nrel.gov/apps/solpos.pl?syear=2005&smonth=1&sday=17&eyear=2005&emonth=1&eday=17&step=1&stepunit=1&latitude=1.111&longitude=2.222&timezone=3.333&press=4.444&temp=5.555&aspect=6.666&tilt=7.777&solcon=8.888&sbwid=9.999&sbrad=12&sbsky=.34&interval=56&field=34&field=2&zip=0

    url = ''.join(['https://midcdmz.nrel.gov/apps/solpos.pl?',
                   'syear={}'.format(year),
                   '&smonth={}'.format(month),
                   '&sday={}'.format(day),
                   '&eyear={}'.format(year),
                   '&emonth={}'.format(month),
                   '&eday={}'.format(day),
                   '&step=1&stepunit=1&latitude={}'.format(lat),
                   '&longitude={}'.format(lon),
                   '&timezone={}'.format(get_timezone(lat, lon, year, month, day)),
                   '&press=1030&temp=23&aspect=180&tilt=0',
                   '&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04',
                   '&interval=0&field=34&field=2&zip=0'])

    page = requests.get(url)
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
