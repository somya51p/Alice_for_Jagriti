from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', userlogin, name='login'),
    path('signup/', signup1, name='signup'),
    path('', index, name='index')

]
