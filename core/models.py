from django.db import models
from django.conf import settings
# Create your models here.
class Catagories(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    detail = models.TextField(max_length=5000, blank=True, null=True)
    photo = models.ImageField(
        upload_to='catagories_photos/', verbose_name=u"Add image (optional)",
        blank=True, null=True
    )


class Feedback(models.Model):
    fullname = models.CharField(max_length=150, db_index=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    question = models.CharField(max_length=150, blank=True, null=True)
    


class Partner(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    email = models.CharField(max_length=150, db_index=True)
    photo = models.ImageField(
        upload_to='catagories_photos/', verbose_name=u"Add image (optional)",
        blank=True, null=True
    )
    number = models.CharField(max_length=150, db_index=True)
    facebook = models.CharField(max_length=150, db_index=True)