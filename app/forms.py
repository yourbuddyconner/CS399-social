from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import *


class AuthForm(AuthenticationForm):

    def confirm_login_allowed(self, user):
        # auths everyone with valid creds, could be pickier
        pass


class SignupForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class PictureUploadForm(forms.Form):
    image = forms.FileField(label='Upload Your Profile Picture')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['caption', ]
        labels = {
            'caption': ('Say something!'),
        }
