from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import UserProfile, BusinessProfile, Adress, Service, ServiceCategory
from users.api.serializers import ServiceCategorySerializer, UserSerializer, ServiceSerializer, CreateUserSerializer


class UserTestCase(APITestCase):

	def setUp(self):
		self.user2 = User.objects.create(
			email='user@user.com',
			first_name='maros',
			password='maros',
		)

		self.user1 = User.objects.create(
			email='user1@user.com',
			username='marosBe',
			first_name='maros1',
			password='maros1',
		)

		self.serviceCategory1 = ServiceCategory.objects.create(
			name='Hairs'
		)

		self.serviceCategory = ServiceCategory.objects.create(
			name='MakeUp'
		)

	def test_get_user(self):
		url = "/users/api/all/"

		response = self.client.get(url)
		result = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(result, object)
		self.assertEqual(result[0]["email"], "user@user.com")

	def test_post_ServiceCategory(self):
		url = "/users/api/categories/"

		data = {
			"name": "Nails"
		}

		response = self.client.post(url, data=data)
		result = response.json()

		self.assertEqual(response.status_code, 201)
		self.assertEqual(result["name"], "Nails")

	def test_get_ServiceCategory(self):
		url = "/users/api/categories/"

		response = self.client.get(url)
		result = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(result, object)
		self.assertEqual(result[1]["name"], "MakeUp")

	def test_get_single_ServiceCategory(self):
		url = "/users/api/categories/category/1/"

		response = self.client.get(url)
		result = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(result, object)
		self.assertEqual(result["name"], "Hairs")

	def test_patch_ServiceCategory(self):
		url = "/users/api/categories/category/1/"

		data = {
			'name': 'Hairs Updated'
		}

		response = self.client.patch(url, data=data)
		result = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(result, object)
		self.assertEqual(result["name"], "Hairs Updated")


	def test_delete_ServiceCategory(self):
		url = "/users/api/categories/category/2/"

		response_del = self.client.delete(url)
		response_get = self.client.delete(url)
		result = response_get.json()

		self.assertEqual(response_del.status_code, 204)
		self.assertEqual(response_get.status_code, 404)

	def test_post_Service(self):

		url = "/users/api/categories/services/"

		data = {
			"user": self.user1.id,
			"category": self.serviceCategory.id,
			"name": "HairCut",
			"service": "HairCut",
			"length": 12,
			"price": 20.00
		}

		response = self.client.post(url, data=data)
		result = response.json()

		self.assertEqual(response.status_code, 201)
		self.assertIsInstance(result, object)
		self.assertEqual(result["name"], "HairCut")


