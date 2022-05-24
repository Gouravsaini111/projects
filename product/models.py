import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from Base.base_files import customer_profile_pic_upload, product_image_upload
# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to=customer_profile_pic_upload, null=True, blank=True)

    class Meta:
        ordering = ('-date_joined',)


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=product_image_upload, null=True, blank=True)

    class Meta:
        ordering = ('name',)








