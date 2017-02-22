from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):	
	randomId= models.IntegerField()  
	birth_date = models.DateField(null=True, blank=True)
	