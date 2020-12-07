from django.urls import  path
from .views import *


app_name = 'Book'
urlpatterns = [
    path('', chapter_index, name='chapters'),
    path('chap<num>/', chapter, name='chapter_name'),
]