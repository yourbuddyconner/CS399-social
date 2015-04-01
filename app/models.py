# Django auth form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
	owner = models.ForeignKey(User);
	post_type = models.CharField(max_length=100) #Is this needed?
	caption = models.CharField(max_length=300)
	timestamp = models.DateTimeField(auto_now_add=True)

	
	
class Image(models.Model):
	image = models.FileField(upload_to = '/app/static/images')

	# returns a friendly name for django
	def __unicode__(self):
		return self.post_type

