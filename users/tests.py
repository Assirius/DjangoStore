from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {
            'first_name': 'User1', 'last_name': 'Empty',
            'username': 'user1', 'email': 'user@yandex.ru',
            'password1': 'Qwerty1!', 'password2': 'Qwerty1!',
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self._common_tests(response)

    def test_user_registration_post_success(self):

        # check before creation user
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(path=self.path, data=self.data)

        # check after creation user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # check email verification
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_errors(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self._common_tests(response)
        self.assertContains(response=response, text='Пользователь с таким именем уже существует.', html=True)

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)


class UserLoginViewTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='user1',
            email='testuser@example.com',
            password='Qwerty1!'
        )
        self.path = reverse('users:login')

    def test_user_login_get(self):
        response = self.client.get(self.path)

        self._common_tests(response)

    def test_user_login_post_success(self):
        response = self.client.post(path=self.path, data={
            'username': 'user1',
            'password': 'Qwerty1!',
        })

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('index'))

    def test_user_login_post_errors(self):
        response = self.client.post(path=self.path, data={
            'username': 'userError',
            'password': 'Qwerty1!',
        })

        self._common_tests(response)
        self.assertTrue(response.context['form'].errors)
        self.assertContains(html=True,
                            response=response,
                            text='Пожалуйста, введите правильные имя пользователя и пароль. '
                                 'Оба поля могут быть чувствительны к регистру.')

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Авторизация')
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIsInstance(response.context['form'], UserLoginForm)
