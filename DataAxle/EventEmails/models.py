from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    date_of_birth = models.DateField(null=True)
    date_of_joining = models.DateField(null=True)


EVENT_TYPES = [('WA', 'Work Anniversary'),
               ('B', 'Birthday')]


class EmailTemplates(models.Model):
    event_type = models.CharField(max_length=5, choices=EVENT_TYPES)
    email_template = models.TextField()


class EmailLogs(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    is_successful = models.BooleanField()
    email_sent = models.DateTimeField(auto_now_add=True)
