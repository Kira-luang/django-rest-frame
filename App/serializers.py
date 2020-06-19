from rest_framework import serializers

from App.models import User , Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['owner' , 'address']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'id' , 'password']
