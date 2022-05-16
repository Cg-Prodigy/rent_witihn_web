from distutils.log import Log
from django.urls import path
from .views import HomePage,LoginSignUp


urlpatterns=[
    path('',HomePage,name='home_page'),
    path('login',LoginSignUp, name='login-signup')
]