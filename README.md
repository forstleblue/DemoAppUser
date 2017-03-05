# UserManager
This script extend User Model in Django. Add edit, delete, view the user.
To extend User in Django there are many ways.
I used the following methods.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):	
	randomId= models.IntegerField()  
	birthday = models.DateField(null=True, blank=True)
	
The project has three basic apps:

Feed (A Twitter-like microblog)
Articles (A collaborative blog)
Question & Answers (A Stack Overflow-like platform)
  
In this way I extend the user, when use this method, you should create models.py at first after create the project.

Feed App

The Feed app has infinite scrolling, activity notifications, live updates for likes and comments, and comment tracking.

Articles App

The Articles app is a basic blog, with articles pagination, tag filtering and draft management.

Question & Answers App

The Q&A app works just like Stack Overflow. You can mark a question as favorite, vote up or vote down answers, accept an answer and so on.

Technology Stack

Python 2.7 / 3.5
Django > 1.9
Twitter Bootstrap 3
jQuery 2


To run this app in terminal or console widnow
go to the this app script directory run following command

python manage.py runserver

The log in redirect page is localhost:8000/feeds/
