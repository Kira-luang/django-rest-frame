from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework import exceptions

from Authentication.models import User


class UserAuthentication(BaseAuthentication):
    '''认证用户是否登录'''

    def authenticate(self , request):
        if request.method == 'GET':
            try:
                token = request.query_params.get('token')
                userid = cache.get(token)
                user = User.objects.get(id=userid)
                return user , token
            except:
                raise exceptions.NotAuthenticated


class UserPermission(BasePermission):
    '''认证用户权限'''

    def has_permission(self , request , view):
        if request.method == 'GET':
            return request.user.is_super
        else:
            return True
