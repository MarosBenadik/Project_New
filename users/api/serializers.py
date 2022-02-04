import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from django.core import exceptions
from users.models import ServiceCategory, Service
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError


class ServiceCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceCategory
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups', 'date_joined']


class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = AbstractUser
		fields = ('email', 'first_name', 'last_name', 'password', 'password2', 'groups')

	def validate_password(self, value):
		try:
			validate_password(value)
		except ValidationError:
			raise serializers.ValidationError(str(ValidationError))
		return value

	def create(self, validated_data):
		user = super().create(validated_data)
		user.set_password(validated_data['password'])
		groups_data = validated_data.pop('groups')
		for group_data in groups_data:
			user.groups.add(group_data)

		user.is_active = False
		user.save ()
		return user

	def update (self, instance, validated_data):
		user = super().update(instance, validated_data)
		if 'password' in validated_data:
			user.set_password(validated_data['password'])
			user.save()
		return user