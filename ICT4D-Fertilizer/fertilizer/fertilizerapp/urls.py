from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/fertilizer/$', views.add_fertilizer, name='add_fertilizer'),
    url(r'^add/crop/$', views.add_crop, name='add_crop'),
    url(r'^add/weather/$', views.add_weather, name='add_weather'),

    url(r'^fertilizer/(?P<id>\d+)/edit/$', views.edit_fertilizer, name='edit_fertilizer'),
    url(r'^fertilizer/(?P<id>\d+)/$', views.fertilizer, name='fertilizer'),
    url(r'^', views.index, name='index'),

]