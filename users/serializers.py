from django.db import models
from django.db.models import fields
from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email',
                  'role')
        extra_kwargs = { 
            'password': {'required': False}, 
            'email': {'required': True} 
        }