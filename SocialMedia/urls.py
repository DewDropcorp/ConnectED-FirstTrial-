from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='SocialMedia'),
    path('home', views.home, name="home"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus"),
    path('ConnectED', views.ConnectED, name='ConnectED'),
    path('signup', views.Signup, name="signup"),
    path('login', views.Login, name = 'login'),
    path('index', views.index, name="index")
]