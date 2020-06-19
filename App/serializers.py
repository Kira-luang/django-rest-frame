from rest_framework import serializers

from App.models import User , Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['owner' , 'address']


class UserSerializer(serializers.ModelSerializer):
    address_set = AddressSerializer(many=True , read_only=True)
    class Meta:
        model = User
        fields = ['username' , 'id' , 'password' , 'address_set']
