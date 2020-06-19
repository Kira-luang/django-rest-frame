from django.core.cache import cache
from rest_framework.throttling import UserRateThrottle

from App.models import User


class UserThrottle(UserRateThrottle):
    scope = 'user'

    def get_cache_key(self , request , view):
        if isinstance(request.user , User):
            ident = request.auth
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope ,
            'ident': ident
        }


class AddressRateThrottle(UserRateThrottle):
    scope = 'address'

    def get_cache_key(self , request , view):
        if isinstance(request.user , User):
            ident = request.auth
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope ,
            'ident': ident
        }
