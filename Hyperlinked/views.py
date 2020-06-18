from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User , Group
from rest_framework import viewsets

from Hyperlinked.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
