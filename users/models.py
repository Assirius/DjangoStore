from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images/%Y/%m/%d/', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verify_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        html_message = 'Для подтверждение учетной записи пользователя {}, перейдите по <a href="{}">ссылке</a>'.format(
            self.user.username,
            verify_link
        )

        send_mail(
            subject=subject,
            message=None,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
            html_message=html_message
        )

    def is_expired(self):
        return now() >= self.expiration
