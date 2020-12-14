from rest_framework import serializers

from .models import Register, Signin

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'name', 'password')

class SigninSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signin
        fields = ('name', 'password')