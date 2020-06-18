from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer

from Authentication.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'name' , 'is_super' , 'is_delete' , 'password']
