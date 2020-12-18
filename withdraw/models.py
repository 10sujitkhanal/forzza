from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Withdraw(models.Model):
    withdraw_amount = models.CharField(max_length=150, db_index=True)
    frozza_username = models.SlugField(max_length=150, null=True, blank=True)
    review = models.TextField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='withdraw_user', on_delete=models.CASCADE)
    status = models.BooleanField(default=False, db_index=True)
    date = models.DateTimeField(default=timezone.now)
