from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from Users.models import User
from datetime import datetime, date
from django.db import models
import random
# Create your models here.

class SignUpForm(forms.ModelForm):
	username = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=30,
		required=True,
		help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')  # noqa: E261
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	confirm_password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
		label="Confirm your password",
		required=True)
	email = forms.CharField(
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
		required=True,
		max_length=75)
	birthday = forms.DateField(
		widget=forms.DateInput(attrs={'class': 'form-control'}),
		initial=date.today,
		required=True,
		)
	randomId = forms.IntegerField(
		widget=forms.NumberInput(attrs={'class': 'form-control'}),
		initial=random.randint(1, 100),
		required=True)

	class Meta:
		ordering =['id']
		model = User
		fields = ['username', 'password', 'confirm_password', 'email', 'birthday', 'randomId']

	def clean(self):
		super(SignUpForm, self).clean()
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		email = self.cleaned_data.get('email')
		birthday = self.cleaned_data.get('birthday')
		randomId = self.cleaned_data.get('randomId')
		if password and password != confirm_password:
			self._errors['password'] = self.error_class(
				['Passwords don\'t match'])
			return self.cleaned_data



