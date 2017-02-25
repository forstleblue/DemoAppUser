from django import forms
from django.contrib.auth.models import User
from Users.models import User
from datetime import datetime, date
from django.db import models

class UserForm(forms.ModelForm):
	birthday = forms.DateField(initial=date.today)        
	randomId = forms.IntegerField(min_value=1, max_value=100)
	username = forms.CharField(max_length = 255)
	password = forms.CharField(max_length = 50)

	class Meta:
		ordering = ['id']
		model = User
		fields = ['birthday',  'randomId', 'username', 'password']
	
	def clean(self):
		super(UserForm, self).clean()		
		birthday = self.cleaned_data.get('birthday')
		randomId = self.cleaned_data.get('randomId')
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')