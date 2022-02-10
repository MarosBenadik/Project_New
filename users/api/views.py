from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from users.models import ServiceCategory, UserProfile, Service
from rest_framework.response import Response
from .serializers import ServiceCategorySerializer, PhotoSerializer, ProfileLogInSerializer, UpdateProfileSerializer, UserSerializer, ServiceSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import generics


class CategoryList(APIView):
	def get(self, request, format=None):
		category = ServiceCategory.objects.all()
		serializer = ServiceCategorySerializer(category, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = ServiceCategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleCategory(APIView):
	def get_object(self, pk):
		try:
			return ServiceCategory.objects.get(pk=pk)
		except ServiceCategory.DoesNotExist:
			raise Http404


	def get (self, request, pk, format=None):
		category = self.get_object(pk)
		serializer = ServiceCategorySerializer(category)
		return Response(serializer.data)


	def patch(self, request, pk, format=None):
		category = self.get_object(pk)
		serializer = ServiceCategorySerializer(category, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		category = self.get_object(pk)
		category.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(APIView):
	def get(self, request):
		users = UserProfile.objects.all()
		serializer = ProfileSerializer(users, many=True)
		return Response(serializer.data)

class ServicesView(APIView):
	def get(self, request):
		service = Service.objects.all()
		serializer = ServiceSerializer(service, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ServiceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save ()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkingHoursView(APIView):
	def get(self, request):
		working_days = WorkingDays.objects.all()
		serializer = WorkingDaysSerializer(working_days, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = WorkingDaysSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save ()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUser(APIView):

	def get(self, request, pk, format=None):
		user = UserProfile.objects.get(pk=pk)
		serializer = ProfileSerializer(user)
		return Response (serializer.data)

	def patch(self, request, pk, format=None):
		user = User.objects.get(pk=pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		user = UserProfile.objects.get(pk=pk)
		serializer = UpdateProfileSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = User.objects.get(pk=pk)
		user.delete()
		return Response (status=status.HTTP_204_NO_CONTENT)


class RegisterAPI(generics.GenericAPIView):
	permission_classes = [permissions.AllowAny]
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		userprofile = UserProfile.objects.create(user=user)

		return Response({
			"user": UserSerializer(user, context=self.get_serializer_context()).data,
		})


class LoginAPI(generics.GenericAPIView):
	permission_classes = [permissions.AllowAny]
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data

		def profile_info(user):
			profile = UserProfile.objects.get(pk=user.pk)
			serializer = ProfileLogInSerializer(profile)

			return {
		        'profile_info': serializer.data,
	        }

		def get_tokens_for_user(user):
			refresh = RefreshToken.for_user(user)

			return {
		        'refresh': str (refresh),
		        'access': str (refresh.access_token),
	        }

		tokens = get_tokens_for_user(user)

		profile = profile_info(user)

		return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
	        "profile": profile,
	        "tokens": tokens,

        })


class GetAllPhotos(APIView):
	def get(self, request, pk, format=None):
		user = UserProfile.objects.get(pk=pk)
		pictures = user.images
		serializer = PhotoSerializer(pictures, many=True)
		return Response (serializer.data)

	def post(self, request, pk, format=None):
		user = UserProfile.objects.get(pk=pk)
		serializer = PhotoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			user.images.add(serializer.data['id'])
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		pictures = user.image
		serializer = PhotoSerializer (pictures, many=True)