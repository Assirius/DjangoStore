import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailVerification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expirations = now() + timedelta(hours=48)
    verification = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expirations)
    verification.send_verification_email()
