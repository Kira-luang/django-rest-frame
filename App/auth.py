from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from App.models import User


class Authentication(BaseAuthentication):
    def authenticate(self , request):
        try:
            token = request.query_params.get('token')
            userid = cache.get(token)
            user = User.objects.get(id=userid)
            if isinstance(user , User):
                return user , token
        except:
            raise exceptions.AuthenticationFailed
