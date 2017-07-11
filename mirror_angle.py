from web_scrape import get_dict
from math import atan2, degrees
from datetime import datetime as dt


def get_date_location():
    if 'y' in input("Use current date? (y/n) ").lower():
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

    # h and d are height and horiz. distance of mirror to target
    # TODO replace set values with inputs
    h = 8
    d = 5

    return (degrees(atan2(h, d)) - data[time]['altitude']) / 2


for i in range(6, 19):
    time = '{}:00:00'.format(i)
    # time_data = data[time]
    print(time + ':', 'altitude:', data[time]['altitude'], 'd:', vert_angle(time))
