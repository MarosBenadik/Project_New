from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from users.models import ServiceCategory, UserProfile, Service
from rest_framework.response import Response
from .serializers import ServiceCategorySerializer, UserSerializer, ServiceSerializer, CreateUserSerializer
from rest_framework import status
from django.contrib.auth.models import User


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
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
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

class GetUser(APIView):

	def get(self, reques, pk, format=None):
		user = User.objects.get(pk=pk)
		serializer = UserSerializer(user)
		return Response (serializer.data)


class CreateUser(APIView):

	def post(self, request):
		serializer = CreateUserSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)




