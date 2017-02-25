from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):	
	randomId= models.IntegerField()  
	birthday = models.DateField(null=True, blank=True)
	