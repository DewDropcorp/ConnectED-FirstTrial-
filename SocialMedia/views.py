from ast import Pass
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'Home.html')

def aboutus(request):
    return render(request, 'AboutUs.html')

def contactus(request):
    return render(request, 'Contactus.html')

def ConnectED(request):
    return render(request, 'ConnectED.html')

def Login(request):
    return render(request, 'signin.html')

def index(request):
    return render(request, 'index.html')

def Signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page

                #create a profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


