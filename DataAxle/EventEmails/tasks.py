from celery import shared_task

from django.core.mail import send_mail


@shared_task()
def send_email():
    send_mail(
        "Subject here",
        "Here is the message.",
        "dataaxle794@gmail.com",
        ["dhirajcdri@gmail.com"],
        fail_silently=False, )
    return None
