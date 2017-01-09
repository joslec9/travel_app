from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.travel, name= 'travel'),
    url(r'^createprocess$', views.createTravel, name = 'createTravel'),
    url(r'^create$', views.createTravelForm, name= 'createTravelForm'),
    url(r'^(?P<tripID>\d+)/delete$', views.deleteTravel, name = 'deleteTravel'),
	url(r'^(?P<tripID>\d+)/info$', views.tripInfo, name="tripInfo"),
	url(r'^(?P<tripID>\d+)/join$', views.joinTravel, name="joinTravel"),
]