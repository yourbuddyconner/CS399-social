from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def directions(request):
    return render(request, 'directions.html')

def merchandise(request):
    return render(request, 'merchandise.html')

def tickets(request):
    return render(request, 'tickets.html')

def schedule(request):
    return render(request, 'schedule.html')