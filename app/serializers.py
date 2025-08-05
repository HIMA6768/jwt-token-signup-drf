from rest_framework import serializers
from .models import userdatatable

from django.contrib.auth.models import User

class userdataserializer(serializers.ModelSerializer):
    class Meta:
        model=userdatatable
        fields='__all__'

class signupserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']