from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'Home.html')

def aboutus(request):
    return render(request, 'AboutUs.html')

def contactus(request):
    return render(request, 'Contactus.html')

def ConnectED(request):
    return render(request, 'ConnectED.html')


