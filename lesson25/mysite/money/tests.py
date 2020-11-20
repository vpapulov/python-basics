from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Account


class TestAccount(TestCase):
    ACCOUNT_NAME = 'тестовый кошелек'

    def setUp(self):
        self.account = Account.objects.create(name=self.ACCOUNT_NAME)

    def tearDown(self):
        self.account.delete()

    def test_str(self):
        self.assertEqual(self.account.name, self.ACCOUNT_NAME)
        self.assertEqual(Account.objects.count(), 1)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
        self.staff = User.objects.create_user('staff', 'staff@test.com', 'staff123', is_staff=True)
        self.user = User.objects.create_user('user', 'user@test.com', 'user123')

    def test_create_account(self):
        response = self.client.get(reverse('money:account-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['object_list'])

    def test_rights(self):
        create_url = reverse('money:account-create')
        # anonymous should have no access
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 302)
        # admin access
        self.client.force_login(self.admin)
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        # staff access
        self.client.force_login(self.staff)
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        # user should have np access
        self.client.force_login(self.user)
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 403)
        self.client.logout()
