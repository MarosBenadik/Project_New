import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.core import exceptions
from users.models import ServiceCategory, Service, Image, UserProfile, Business, WorkingDays, Adress, SubServices
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError



class WorkingDaysSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkingDays
		fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups', 'date_joined']



class AdressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Adress
		fields = '__all__'


class ServiceCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ServiceCategory
		fields = '__all__'


class SubServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubServices
		fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
	category = ServiceCategorySerializer(many=True)
	service = SubServiceSerializer(many=True)
	class Meta:
		model = Service
		fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
	services = ServiceSerializer(many=True)
	working_days = WorkingDaysSerializer(many=True)
	class Meta:
		model = Business
		fields = '__all__'


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'groups')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

    def profile_create(self, validated_data):
	    userprofile = UserProfile.objects.create(user=validated_data['id'], username=validated_data['username'])
	    return userprofile

# Login Serializer
class LoginSerializer(serializers.Serializer):

	username = serializers.CharField()
	password = serializers.CharField()

	permission_classes = [IsAuthenticated]

	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError("Incorrect Credentials")


class FollowSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('id', 'username', 'name', 'profilepicture', 'bussiness')


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	location = AdressSerializer()
	bussiness = BusinessSerializer()
	followers = FollowSerializer(many=True)
	followings = FollowSerializer(many=True)


	class Meta:
		model = UserProfile
		fields = '__all__'

class UpdateProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = (
			'bio','birth_date','location','name'
		)

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'


class ProfileLogInSerializer(serializers.ModelSerializer):
	location = AdressSerializer ()
	bussiness = BusinessSerializer ()
	followers = FollowSerializer (many=True)
	followings = FollowSerializer (many=True)

	class Meta:
		model = UserProfile
		fields = '__all__'
