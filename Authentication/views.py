import uuid

from django.core.cache import cache
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password , check_password
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

from Authentication.APISettings import UserAuthentication , UserPermission
from Authentication.constant import HTTP_ACTION_REGISTER , HTTP_ACTION_LOGIN
from Authentication.models import User
from Authentication.serializers import UserSerializer
from Django_rest_frame.settings import SUPER_USER


class UsersViewset(ListCreateAPIView):
    queryset = User.objects.filter(is_delete=False)
    serializer_class = UserSerializer
    authentication_classes = (UserAuthentication ,)
    permission_classes = (UserPermission ,)

    # def get(self, request, *args, **kwargs):
    #     if isinstance(request.user, User):
    #         return self.list(request , *args , **kwargs)
    #     else:
    #         raise exceptions.NotAuthenticated

    def post(self , request , *args , **kwargs):
        if request.query_params.get('action') == HTTP_ACTION_REGISTER:
            return self.create(request , *args , **kwargs)
        elif request.query_params.get('action') == HTTP_ACTION_LOGIN:
            name = request.data.get('name')
            password = request.data.get('password')
            print(name , password)
            try:
                user = User.objects.get(name=name)
                if user.password == password:
                    token = uuid.uuid4().hex
                    cache.set(token , user.id)
                    data = {
                        'token': token ,
                        'msg': 'login success' ,
                        'status': 200
                    }
                    return Response(data=data)  # 发送token给客户端
                else:
                    return exceptions.AuthenticationFailed
            except:
                return exceptions.NotFound
        else:
            return exceptions.NotFound

    def create(self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        if request.data['name'] in SUPER_USER:
            user = User.objects.get(name=request.data['name'])
            user.is_super = True
            user.save()
            data['is_super'] = True
        headers = self.get_success_headers(data)
        return Response(data , status=status.HTTP_201_CREATED , headers=headers)


class UserViewset(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_delete=False)
    serializer_class = UserSerializer
