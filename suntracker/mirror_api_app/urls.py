from django.conf.urls import url
from . import views


# url_string = ('^api/'
#               '(?P<height>\d+(.\d+)?)?'
#               '(?P<distance>\d+(.\d+)?)?'
#               '(?P<year>\d{4})?'
#               '(?P<month>\d{1,2})?'
#               '(?P<day>\d{1,2})?'
#               '(?P<latitude>\d+(.\d+)?)?'
#               '(?P<longitude>\d+(.\d+)?)?'
#               '(?P<direction>\d+(.\d+)?)')

urlpatterns = [
    url(r'^options/', views.options, name='options'),
    url(r'^api/(?P<height>\d+(.\d+)?)?(?P<distance>\d+(.\d+)?)?(?P<year>\d{4})?(?P<month>\d{1,2})?(?P<day>\d{1,2})?(?P<latitude>\d+(.\d+)?)?(?P<longitude>\d+(.\d+)?)?(?P<direction>\d+(.\d+)?)', views.api, name='api')
]