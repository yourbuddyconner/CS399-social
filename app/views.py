from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from app.models import *
from app.forms import SignupForm
from app.forms import AuthForm
from app.forms import PictureUploadForm
from app.forms import PostForm


#Rest Framework
from rest_framework import serializers 

#JSON
from django.http import JsonResponse

# for login, logout, and auth
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.contrib.auth.models import User

#https://docs.djangoproject.com/en/1.7/topics/auth/default/#the-login-required-decorator
# catch the user if logged out
# redirect to login with the path where they were going


@login_required(login_url='/')
def posts(request):
	postform = PostForm()
	if request.method == 'POST':
		postform = PostForm(request.POST)
		if postform.is_valid():
			x = Post()
			x.owner = request.user
			x.caption = postform.cleaned_data['caption']
			x.save()
		return HttpResponseRedirect('/feed')
	elif request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return (JsonResponse(serializer.data, safe=False, status=200)) #not sure of the implications of safe=false

@login_required(login_url='/')
def feed(request):
	postform = PostForm()
	return render(request, 'feed.html', {'postform': postform})

@login_required(login_url='/')
def temp(request):
    return render(request, 'oldfeed.html')

@login_required(login_url='/')
def explore(request):
    return render(request, 'feed.html')

@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')

def splash(request):
	signupform = SignupForm()
	authform = AuthForm()
	if request.method == 'POST':
		signupform = SignupForm(request.POST)
		if signupform.is_valid():
			if username_exists(signupform.cleaned_data["username"]):
				messages.error(request, 'Username already exists.')
				return render(request, 'splash.html', {'signupform': signupform, 'authform': authform})
			if email_exists(signupform.cleaned_data["email"]):
				messages.error(request, 'User already exists with this email address.')
				return render(request, 'splash.html', {'signupform': signupform, 'authform': authform})
				
			user = User.objects.create_user(signupform.cleaned_data["username"], signupform.cleaned_data["email"], signupform.cleaned_data["password"])
			user.first_name = signupform.cleaned_data["first_name"]
			user.last_name = signupform.cleaned_data["last_name"]
			user.save
			return render(request, 'dashboard.html')
	else:
		signupform = SignupForm()
	return render(request, 'splash.html', {'signupform': signupform, 'authform': authform})


def about(request):
    return render(request,'about.html')

def username_exists(username):
    if User.objects.filter(username=username).count():
        return True
    return False	
	
def email_exists(email):
    if User.objects.filter(email=email).count():
        return True
    return False

def profile_picture(request):
    if request.method == 'POST':
        form = PictureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Image(image = request.FILES['image'])
            instance.save()
            return HttpResponseRedirect('dashboard.html')
    else:
        form = PictureUploadForm()
    return render(request, 'profile_picture.html', {'form': form})
	
# comment
def login(request):
    # catch logged-in user and send them to dash
    #if request.user.is_authenticated():
    #    return redirect('dashboard')
	authform = AuthForm(request.POST)
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			# Redirect to a success page.
			#return render(request, 'dashboard.html')
			return HttpResponseRedirect('/feed')
		else:
			# Return a 'disabled account' error message
			messages.error(request, 'Account is disabled')
			return render(request, 'login.html', {'form': authform})
	else:
		# Return an 'invalid login' error message.
		messages.error(request, 'Incorrect username or password')
		return render(request, 'login.html', {'form': authform})	


def logout(request):
		authform = AuthForm()
		auth_logout(request)
		return render(request, 'login.html', {'form': authform})
		
#Serializers
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('owner', 'caption', 'timestamp')