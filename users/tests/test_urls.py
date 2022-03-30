from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

	def test_categories_url(self):
		url = reverse('categories')

		self.assertEqual(resolve(url).url_name, 'categories')

	def test_category_url(self):
		url = reverse('category', kwargs={'pk': 1})

		self.assertEqual(resolve(url).url_name, 'category')

	def test_users_url(self):
		url = reverse('users')

		self.assertEqual(resolve(url).url_name, 'users')

	def test_user_url(self):
		url = reverse('user', kwargs={'pk': 1})

		self.assertEqual(resolve(url).url_name, 'user')

	def test_services_url(self):
		url = reverse('services')

		self.assertEqual(resolve(url).url_name, 'services')