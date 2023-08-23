from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_email


# Create your views here.

def index(request):
    result = send_email.delay()
    return HttpResponse(f"Hello, world. You're at the polls index {result}.")
