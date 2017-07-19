from web_scrape import get_dict
from math import atan2, degrees
from datetime import datetime as dt
# import pprint


def get_date_location(lat, lon):
    now = dt.now()
    start_year = now.year
    start_month = now.month
    start_day = now.day
    latitude = '35.951053'
    longitude = '-78.544401'
    return locals()


with open('configuration.csv', 'r') as f:
    config = next(f)
height, distance, angle, lat, lon = config.split(',')
data = get_dict(get_date_location(lat, lon))


def vert_angle(time):
    """h and d are height and depth component of
    horiz. distance from mirror to target"""

    # TODO replace set values with inputs
    h = 8
    d = 5
    w = 10

    distance = (d ** 2 + w ** 2) ** 0.5

    return round((degrees(atan2(h, distance)) - data[time]['altitude']) / 2, 4)


def horiz_angle(time):
    """
    returns horizontal angle of mirror in degrees, measured
    clockwise from the apparatus heading, where a_h = 0 means
    the w axis points due north
    """

    # TODO What should 0deg be? Set it to inline w/ target? facing target?

    # TODO replace set values with inputs, don't define d twice
    d = 5
    w = 10

    # direction of the sun. measured in degrees counted clockwise from north.
    azimuth = data[time]['azimuth']

    # adjust azimuth to be relative to direction of mirror setup.
    azimuth -= int(angle)

    # TODO this answer still relies on d and w vars, not on csv values
    h_angle = ((atan2(d, w) + azimuth) / 2 - 90)

    # returns answer between -180 and 180 degrees
    return round(((h_angle + 180) % 360) - 180, 4)


def mirror_api():
    """
    returns dict w/ horiz and vert mirror angles for every minute of daylight
    """

    return {key: {'vertical': vert_angle(key),
                  'horizontal': horiz_angle(key)} for key in data.keys()}


api = mirror_api()

# pprint.pprint(api)

for i in range(7, 21):
    time = "{}:00:00".format(i)
    print("{}:".format(time),
          "Azimuth:", data[time]['azimuth'],
          "Horizontal angle:", api[time]['horizontal'])
