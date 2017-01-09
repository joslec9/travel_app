from __future__ import unicode_literals

from django.db import models

#import models from User
from ..login_registration.models import User

# Create your models here.


class TravelManager(models.Manager):
	def validateTravel(self, post):
		pass

	def addTravel(self, post):
		pass



class Travel(models.Model):
	destination = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	planner = models.ForeignKey(User)
	datestart = models.DateTimeField()
	dateend = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class JoinedTrip(models.Model):
	trip = models.ForeignKey(Travel)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)