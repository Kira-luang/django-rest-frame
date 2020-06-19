from django.contrib import admin
from django.urls import path , include , re_path

from App import views

urlpatterns = [
    re_path('^users/$' , views.UsersViewSet.as_view() , name='users') ,
    re_path('users/(?P<pk>\d+)/' , views.UserViewSet.as_view() , name="user-detail") ,
    re_path('^address/$' , views.AddressViewSet.as_view({'get': 'list' , 'post': 'create'})) ,
    re_path('^address/(?P<pk>\d+)/' , views.AddressViewSet.as_view({'get': 'retrieve'})) ,
]
