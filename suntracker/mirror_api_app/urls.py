from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^options/', views.options, name='options'),
    url(r'^api/height=(?P<height>\d+(.\d+)?)&distance=(?P<distance>\d+(.\d+)?)&year=(?P<year>\d{4})&month=(?P<month>\d{1,2})&day=(?P<day>\d{1,2})&lat=(?P<lat>-?\d+(.\d+)?)&lon=(?P<lon>-?\d+(.\d+)?)&direction=(?P<direction>\d+(.\d+)?)', views.api, name='api'),
    url(r'^get_data/', views.get_data, name='data')
]

# TODO: new endpoint for just sun position?
