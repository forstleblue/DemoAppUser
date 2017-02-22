from django.test import TestCase

# Create your tests here.
from app.models import User

class UserTestCase(TestCase):
	def setUp(self):
		User.objects.create(username="John", password="john", randomId="50")
		User.objects.create(username="Tom", password="123", randomId="39")

	def test_user(self):
		user1 = User.objects.get(username="John")
		user2 = User.objects.get(username="Tom")

		self.assertEqual(user1.password, "john")