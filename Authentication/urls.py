from django.urls import path , re_path

from Authentication import views

urlpatterns = [
    path('users/' , views.UsersViewset.as_view() , name='users') ,
    re_path('users/(?P<pk>\d+)/' , views.UserViewset.as_view() , name='user') ,
]
