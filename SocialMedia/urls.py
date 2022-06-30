from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='SocialMedia'),
    path('home', views.home, name="home"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus"),
    path('ConnectED', views.ConnectED, name='ConnectED'),
    path('signup', views.Signup, name="signup"),
    path('signin', views.Signin, name = 'Signin'),
    path('logout', views.Logout, name='Logout'),
    path('settings', views.Settings, name='settings'),
    path('index', views.index, name="index")
]