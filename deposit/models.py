from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Deposit(models.Model):
    deposit_amount = models.CharField(max_length=150, db_index=True)
    frozza_username = models.SlugField(max_length=150, null=True, blank=True)
    review = models.TextField(max_length=5000, blank=True, null=True)
    photo = models.ImageField(
        upload_to='deposit_photos/', verbose_name=u"Add image (optional)",
        blank=True, null=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='deposit_user', on_delete=models.CASCADE)
    status = models.BooleanField(default=False, db_index=True)
    date = models.DateTimeField(default=timezone.now)
