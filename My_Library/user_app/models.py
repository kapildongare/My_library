from django.db import models



# Create your models here.
class UPerson(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(null=True, unique=True)
    is_active = models.BooleanField(default=True)