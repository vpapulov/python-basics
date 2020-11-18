from django.test import TestCase, Client
from django.contrib.auth.models import User
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
        self.ADMIN_PASS = 'admin123'
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', self.ADMIN_PASS)
        self.STAFF_PASS = 'staff123'
        self.staff = User.objects.create_user('staff', 'staff@test.com', self.STAFF_PASS, is_staff=True)
        self.USER_PASS = 'user123'
        self.user = User.objects.create_user('user', 'user@test.com', self.USER_PASS)

    def test_create_account(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['my_var'], '123')

    def test_rights(self):
        # anonymous should have no access
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 302)
        # admin access
        self.client.login(username='admin', password=self.ADMIN_PASS)
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        # staff access
        self.client.login(username='staff', password=self.STAFF_PASS)
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        # user should have np access
        self.client.login(username='user', password=self.USER_PASS)
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 403)
        self.client.logout()
