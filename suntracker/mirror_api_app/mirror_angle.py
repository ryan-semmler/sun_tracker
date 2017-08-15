from .web_scrape import get_dict
from math import atan2, degrees


def vert_angle(time, data, height, distance):

    altitude = float(data[time]['altitude'])
    height = float(height)
    distance = float(distance)

    return round((degrees(atan2(height, distance)) - altitude) / 2, 4)


def horiz_angle(time, data):
    """
    returns horizontal angle of mirror in degrees, measured
    clockwise from the apparatus heading, where a_h = 0 means
    the w axis points due north
    """

    # TODO: What should 0deg be? Set it to inline w/ target? facing target?

    # direction of the sun. measured in degrees counted clockwise from north.
    azimuth = data[time]['azimuth']

    h_angle = (azimuth / 2 - 90)

    # returns answer between -180 and 180 degrees
    return round(((h_angle + 180) % 360) - 180, 4)


def mirror_api(data, height, distance):
    """
    returns dict w/ horiz and vert mirror angles for every minute of daylight
    """

    return {time: {'vertical': vert_angle(time, data, height, distance),
                   'horizontal': horiz_angle(time, data)} for time in data.keys()}


def main(height, distance, year, month, day, lat, lon, direction):
    data = get_dict(year, month, day, lat, lon)
    api = mirror_api(data, height, distance)
    return api

    # for i in range(7, 21):
    #     time = "{}:00:00".format(i)
    #     print("{}:".format(time),
    #           degrees(atan2(distance, height)) + api[time]['vertical'] -
    #           (90-(data[time]['altitude'] + api[time]['vertical'])))
