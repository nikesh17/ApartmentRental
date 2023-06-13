from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Apartment(models.Model):
    apartment_id = models.IntegerField(null=False, unique=True)
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images', default="")
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.apartment_id)

