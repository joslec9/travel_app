from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'



#TODO
# store emails lowercase

class UserManager(models.Manager):
	def login(self, postData):
		user_list = User.objects.filter(username=postData['username']) 

		if user_list:
			user = user_list[0]
			#then check their password
			if bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password:
				#login is valid
				return user
		return None



	def register(self, postData):
		encrypted_password =  bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		User.objects.create(name=postData['name'], username=postData['username'], password=encrypted_password)

	def validate_user_info(self, postData):
		errors = []
		if len(postData['name']) == 0:
			errors.append("Name is required")
		elif len(postData['name']) < 2:
			errors.append("Name must be at least 2 characters")
		elif not postData['name'].replace(" ", "").isalpha():
			errors.append("Name must only have letters")


		if len(postData['username']) == 0:
			errors.append("Username is required")
		elif len(postData['username']) < 3:
			errors.append("Username must be longer than 3")


		if postData['email']:
			if not re.match(EMAIL_REGEX, postData['email']):
				errors.append('email must be valid')
		else:
			errors.append('email cannot be empty!')

		if len(postData['password']) == 0:
			errors.append('Password is required')
		elif len(postData['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		elif postData['password'] != postData['passconf']:
			errors.append('Passwords must match')

		if len(User.objects.filter(username=postData['username'])) > 0:
			errors.append("Username is unavailable")
		return errors



# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=45, blank=True, null=True)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()