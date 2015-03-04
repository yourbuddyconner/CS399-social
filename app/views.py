from django.shortcuts import render, redirect
from app.models import *

# for login, logout, and auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    return render(request, 'splash.html')

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