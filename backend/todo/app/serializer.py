from rest_framework import serializers
from .models import AddTodo

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data):
        user=User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddTodo
        fields='__all__'
    