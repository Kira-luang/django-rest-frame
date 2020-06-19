# Create your views here.
import uuid

from django.core.cache import cache
from rest_framework import viewsets , status
from rest_framework.generics import RetrieveAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import exceptions
from rest_framework.response import Response

from App.Throttles import AddressRateThrottle , UserThrottle
from App.auth import Authentication , UserAuthentication
from App.models import User , Address
from App.parameters import HTTP_ACTION_LOGIN , HTTP_ACTION_REGISTER
from App.permissions import UserPermission
from App.serializers import UserSerializer , AddressSerializer


class UsersViewSet(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (UserAuthentication ,)
    throttle_classes = [UserThrottle , ]

    def list(self , request , *args , **kwargs):
        token = request.query_params.get('token')
        userid = cache.get(token)
        queryset = self.filter_queryset(self.queryset.filter(id=userid))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page , many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset , many=True)
        return Response(serializer.data)

    def post(self , request , *args , **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        action = request.query_params.get('actions')
        if username and password:
            if action == HTTP_ACTION_LOGIN:
                try:
                    user = User.objects.get(username=username)
                    if user.password != password:
                        raise exceptions.AuthenticationFailed
                    else:
                        token = uuid.uuid4().hex
                        cache.set(token , user.id)
                        data = {
                            'msg': 'login success' ,
                            'status': 200 ,
                            'token': token
                        }
                        return Response(data)
                except User.DoesNotExist:
                    raise exceptions.AuthenticationFailed
            elif action == HTTP_ACTION_REGISTER:
                User.objects.create(username=username , password=password)
                data = {
                    'msg': 'register success' ,
                    'status': 200 ,
                }
                return Response(data)
            else:
                raise exceptions.AuthenticationFailed
        else:
            raise exceptions.AuthenticationFailed


class UserViewSet(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (Authentication ,)
    permission_classes = (UserPermission ,)
    throttle_classes = [AddressRateThrottle , ]

    def create(self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        address = Address.objects.get(address=data['address'])
        address.owner = request.user
        address.save()
        data['owner'] = request.user.id
        headers = self.get_success_headers(data)
        return Response(data , status=status.HTTP_201_CREATED , headers=headers)

    def list(self , request , *args , **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(owner=request.user.id))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page , many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset , many=True)
        return Response(serializer.data)

    def retrieve(self , request , *args , **kwargs):
        address = Address.objects.get(id=kwargs['pk'])
        if address.owner == request.user.id:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise exceptions.AuthenticationFailed
