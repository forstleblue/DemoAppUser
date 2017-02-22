# UserManager
This script extend User Model in Django. Add edit, delete, view the user.
To extend User in Django there are many ways.
I used the following methods.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):	
	randomId= models.IntegerField()  
	birth_date = models.DateField(null=True, blank=True)
	
  
In this way I extend the user, when use this method, you should create models.py at first after create the project.
