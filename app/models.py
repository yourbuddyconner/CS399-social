# Django auth form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
	owner = models.ForeignKey(User);
	post_type = models.CharField(max_length=100)
	caption = models.CharField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True)

	# returns a friendly name for django
	def __unicode__(self):
		return self.post_type

class Signup(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length = 254)
	username = models.EmailField(max_length = 50)
	password = models.IntegerField()
	created = models.DateTimeField(auto_now_add = True)