# subscription/models.py

from django.db import models
from django.conf import settings

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    permissions = models.ManyToManyField('Permission')
    usage_limit = models.PositiveIntegerField()

class Permission(models.Model):
    name = models.CharField(max_length=100)
    api_endpoint = models.CharField(max_length=100)
    description = models.TextField()

class UserSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    current_usage = models.PositiveIntegerField(default=0)
    custom_usage_limit = models.PositiveIntegerField(default=0)
