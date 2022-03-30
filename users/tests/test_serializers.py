from django.test import TestCase
from users.api.serializers import ServiceCategorySerializer, ServiceSerializer, UserSerializer
from users.models import ServiceCategory
from django.contrib.auth.models import User

class SerializersTestCase(TestCase):

	def setUp(self):
		self.user1 = User.objects.create(
			email='user1@user.com',
			username='marosBe',
			first_name='maros1',
			password='maros1',
		)

		self.category = ServiceCategory.objects.create(
			name= 'Nails'
		)

	def test_serviceCategorySerializer(self):
		self.category_attributes = {
			'name': 'Hair',
		}

		serializer = ServiceCategorySerializer(data=self.category_attributes)
		self.assertEqual(serializer.is_valid(), True)
		self.assertEqual(serializer.data['name'], 'Hair')

	def test_ServiceSerializer(self):

		self.service_attributes = {
			'user': self.user1.id,
			'category': self.category.id,
			'name': 'Hair',
			'service': 'Coloring',
			'length': 2,
			'price': 12.00,
		}

		serializer = ServiceSerializer(data=self.service_attributes)
		self.assertEqual(serializer.is_valid(), True)

		print(serializer.data)

		self.assertEqual(serializer.data['name'], 'Hair')
		self.assertEqual(serializer.data['price'], '12.00')


	def test_user(self):

		self.user = {
			'id': '3',
			'email': 'maros@maros.com',
			'first_name': 'Maros',
			'last_name': 'Benadik',
			'username': 'marosko',
			'groups': ['1']
		}

		serializer = UserSerializer(data=self.user)
		self.assertEqual(serializer.is_valid(), False)

		print(serializer.data)

		self.assertEqual(serializer.data['email'], 'maros@maros.com')
		self.assertEqual(serializer.data['username'], 'marosko')