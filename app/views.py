from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from app.models import *
from app.forms import SignupForm
from app.forms import AuthForm

# for login, logout, and auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#https://docs.djangoproject.com/en/1.7/topics/auth/default/#the-login-required-decorator
# catch the user if logged out
# redirect to login with the path where they were going
@login_required
def feed(request):
    return render(request, 'feed.html')

@login_required
def explore(request):
    return render(request, 'feed.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def splash(request):
	signupform = SignupForm()
	authform = AuthForm()
	return render(request, 'splash.html', {'signupform': signupform, 'authform': authform})


def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            register = Signup()
            register.first_name = form.cleaned_data["first_name"]
            register.last_name = form.cleaned_data["last_name"]
            register.email = form.cleaned_data["email"]
            register.username = form.cleaned_data["username"]
            register.password = form.cleaned_data["password"]
            register.save()

            return HttpResponseRedirect('/about')

    else:
        
        signupform = SignupForm()

    return render(request, 'signup.html', {'form': form})



def login(request):
    # catch logged-in user and send them to dash
    if request.user.is_authenticated():
        return redirect('dashboard')
    if request.method == 'POST':
        # fill the AuthForm with post data
        form = AuthForm(request.POST)
        # if the form is valid
        if form.is_valid():
            # log in
            user = form.save()
            return redirect('dashboard.html')
    else: 
        form = AuthForm()
    return render(request, 'login.html', {
        'form': form
    })

def logout(request):
    return render(request, 'splash.html')