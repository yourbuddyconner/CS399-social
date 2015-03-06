from django import forms


class SignupForm(forms.Form):
	first_name = forms.CharField(label = "First Name")
	last_name = forms.CharField(label = "Last Name")
	email = forms.EmailField(label = "Email")
	username = forms.CharField(label = "Username")
	password = forms.IntegerField(label = "Password")

