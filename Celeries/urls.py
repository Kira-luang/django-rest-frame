from django.contrib import admin
from django.urls import path , include

from Celeries import views

urlpatterns = [
    path('test/' , views.test) ,
    path('testcelery/' , views.test_celery) ,
    path('email/' , views.email) ,
]
