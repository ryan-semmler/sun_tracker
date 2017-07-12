from web_scrape import get_dict
from math import atan2, degrees
from datetime import datetime as dt


def get_date_location():
    # if 'y' in input("Use current date? (y/n) ").lower():
    if True:
        now = dt.now()
        start_year = now.year
        start_month = now.month
        start_day = now.day
    else:
        start_year = input("start year: ")
        start_month = input("start month: ")
        start_day = input("start day: ")

    # currently only supports single-day
    # end_year = input("end year: ")
    # end_month = input("end month: ")
    # end_day = input("end day: ")

    # latitude = input("latitude: ")
    # longitude = input("longitude: ")

    latitude = '35.951053'
    longitude = '-78.544401'
    return locals()


data = get_dict(get_date_location())


def vert_angle(time):
    """h and d are height and depth component of
    horiz. distance from mirror to target"""

    # TODO replace set values with inputs
    h = 8
    d = 5
    w = 10

    distance = (d ** 2 + w ** 2) ** 0.5

    return (degrees(atan2(h, distance)) - data[time]['altitude']) / 2


def horiz_angle(time):
    """
    returns horizontal angle of mirror in degrees, measured
    clockwise from the apparatus heading, where a_h = 0 means
    the w axis points due north
    """

    # TODO replace set values with inputs, don't define d twice
    d = 5
    w = 10

    # direction of the sun. measured in degrees counted clockwise from north.
    azimuth = data[time]['azimuth']

    # adjust azimuth to be relative to direction of mirror setup.
    # TODO add separate file to store configuration info. draw info from file.
    # TODO combine w and d vars into just distance, then get heading separately
    apparatus_heading = 50
    azimuth -= apparatus_heading

    # old answer:
    # return (azimuth + atan2(d, w) - 180) / 2

    return ((atan2(d, w) + azimuth) / 2 - 90) % 360

for i in range(6, 20):
    time = '{}:00:00'.format(i)
    # time_data = data[time]
    print(time + ':',
          'azimuth:', round(data[time]['azimuth'] - 50, 4),
          'angle:', horiz_angle(time))
