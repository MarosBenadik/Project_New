from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile, BusinessProfile, Adress, Service, ServiceCategory


class TestModels(TestCase):
	

	def setUp(self):
		self.user1 = User.objects.create(
			email='user@user.com',
			first_name='maros',
			password='maros',
		)

	def test_UserProfile_on_creation(self):
		self.userProfile1 = UserProfile.objects.create(
			user=self.user1,
			name='maros',
			location='London',
		)

		self.assertEquals(self.userProfile1.location, 'London')

	def test_BusinessProfile_on_creation(self):

		self.address = Adress.objects.create(
			street='111 Hatfield mead',
			city='London',
			postcode='SM45PG'
		)

		self.BusinesProfile1 = BusinessProfile.objects.create(
			businessuser=self.user1,
			business_name='business',
			location=self.address,
		)

		self.assertEquals(self.address.city, 'London')
		self.assertEquals(self.BusinesProfile1.business_name, 'business')

	def test_Service_on_creation(self):
		self.serviceCategory = ServiceCategory.objects.create(
			name='Hair'
		)


		self.service1 = Service.objects.create(
			user=self.user1,
			category=self.serviceCategory,
			name='Long Hairs',
			price=12.00,
		)

		self.assertEquals(self.service1.name, 'Long Hairs')
		self.assertEquals(self.serviceCategory.name, 'Hair')
		self.assertEquals(self.service1.category.name, 'Hair')