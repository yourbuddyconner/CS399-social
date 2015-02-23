from django.db import models
from django.utils import timezone

class Campaign(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	start_date = models.DateField('day the campaign begins')
	end_date = models.DateField('day the campaign ends')

	# returns a friendly name for django
	def __unicode__(self):
		return self.name

class InterestedUser(models.Model):
	# Name
	name = models.CharField(max_length=100)
	# Parts of Street Address
	address_street = models.CharField(max_length=150)
	saddress_city = models.CharField(max_length=150)
	address_state = models.CharField(max_length=150)
	address_zip = models.CharField(max_length=150)
	# Phone Number 
	# taken from http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex]) # validators should be a list
    # E-Mail Address
    email = models.EmailField(max_length=254)

class FruityPebblesForm(ModelForm):
	class Meta:
		model = InterestedUser
		fields = ['name', 'address_city', 'address_state', 'address_zip' 'address_street', 'phone_number', 'email']