# auth/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'].lower(),
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user

# In refresh token rotation, return both access and refresh 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['full_name'] = self.user.full_name
        data['email'] = self.user.email
        data['is_admin'] = self.user.is_admin
        return data
