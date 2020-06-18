from django.contrib import admin
from django.urls import path

from CBV import views

urlpatterns = [
    path('books/' , views.Books.as_view() , name='books') ,
]
