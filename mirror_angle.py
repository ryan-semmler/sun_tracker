from web_scrape import get_dict
from math import atan2, degrees
from datetime import datetime as dt
import pprint


def get_date_location(lat, lon):
    now = dt.now()
    start_year = now.year
    start_month = now.month
    start_day = now.day
    latitude = lat
    longitude = lon
    return locals()


# TODO account for users who haven't run config yet
with open('configuration.csv', 'r') as f:
    config = next(f)
values = [float(item) for item in config.split(',')]
height, distance, angle, lat, lon = values
data = get_dict(get_date_location(lat, lon))


def vert_angle(time):
    """h and d are height and depth component of
    horiz. distance from mirror to target"""

    altitude = float(data[time]['altitude'])

    return round((degrees(atan2(height, distance)) - altitude) / 2, 4)


def horiz_angle(time):
    """
    returns horizontal angle of mirror in degrees, measured
    clockwise from the apparatus heading, where a_h = 0 means
    the w axis points due north
    """

    # TODO What should 0deg be? Set it to inline w/ target? facing target?

    # direction of the sun. measured in degrees counted clockwise from north.
    azimuth = data[time]['azimuth']

    h_angle = (azimuth / 2 - 90)

    # returns answer between -180 and 180 degrees
    return round(((h_angle + 180) % 360) - 180, 4)


def mirror_api():
    """
    returns dict w/ horiz and vert mirror angles for every minute of daylight
    """

    return {key: {'vertical': vert_angle(key),
                  'horizontal': horiz_angle(key)} for key in data.keys()}


api = mirror_api()

pprint.pprint(api)

# for i in range(7, 21):
#     time = "{}:00:00".format(i)
#     print("{}:".format(time),
#           "Altitude:", data[time]['altitude'],
#           "Vertical angle:", api[time]['vertical'])
