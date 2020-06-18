from django.urls import path , re_path

from APIViews import views

urlpatterns = [
    path('students/' , views.StudentsViews.as_view() , name='students') ,
    re_path('students/(?P<pk>\d+)' , views.StudentViews.as_view() , name='student') ,
]
