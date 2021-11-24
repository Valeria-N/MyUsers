from rest_framework import serializers
from ..models import User
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['number', 'lastname', 'firstname', 'patronymic', 'address', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    @transaction.atomic
    def update(self, instance, validated_data):
        password = None
        if 'password' in validated_data:
            password = validated_data.pop('password')
        user = super(UserSerializer, self).update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create(self, validated_data):
        password = validated_data.pop('password')
        number = validated_data.pop('number')
        user = User.objects.create_user(number=number, password=password, **validated_data)
        return user

