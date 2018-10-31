from rest_framework.serializers import ModelSerializer

from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'role',
            'city',
        ]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'role',
            'city',
        ]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'reviewer',
            'assigned'
        ]


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'reviewer',
            'assigned'
        ]
