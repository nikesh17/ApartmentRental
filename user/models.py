from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True, null=False)
#     email = models.EmailField(unique=True, null=False)
#     password = models.CharField(max_length=100, null=False)
#     first_name = models.CharField(max_length=100, null=False)
#     last_name = models.CharField(max_length=100, null=False)
#     date_of_birth = models.DateField(null=False)
#     gender = models.CharField(max_length=10, null=False)
#     phone_number = models.CharField(max_length=20, null=False, unique=True)
#     address = models.CharField(max_length =250,null=False)
    
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=False, unique=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    


