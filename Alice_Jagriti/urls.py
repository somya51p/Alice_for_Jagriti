from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from notes.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', userlogin, name='login'),
    path('signup/', signup1, name='signup'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('', index, name='index'),
    path('Book/', include('Book.urls')),

]
