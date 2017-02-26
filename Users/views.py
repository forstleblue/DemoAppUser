from django.shortcuts import render
import random
from django.shortcuts import render, redirect
from Users.models import User
from Users.forms import UserForm
from django.http import HttpResponse
from datetime import *
from django.http import HttpResponseRedirect, StreamingHttpResponse
import csv
from Users.templatetags.oldFilter import oldRange, checkBizzFuzz
from django.contrib import messages

# Create your views here.


def listAllUser(request):
	allUser = User.objects.order_by('-date_joined')
	count = allUser.count()	
	
	return render(request, 'Users/userList.html', {'list':allUser, 'username':request.user.username})

def addUser(request):

	#import pdb; pdb.set_trace()
	randomId = random.randint(1, 100)
	birthday = datetime.today().date()
	context_dict = {}
	context_dict['username'] = ""
	context_dict['password'] = ""
	context_dict['randomId'] = randomId
	context_dict['birthday'] = birthday
	
	return render(request, 'Users/add.html', context_dict)

def editUser(request, userId):
	#import pdb; pdb.set_trace()
	user = User.objects.get(id=userId)		
	return render(request, 'Users/edit.html', {'user': user})



def downloadUserlist(request):
	
	allUser = User.objects.all()

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv" '

	writer = csv.writer(response)

	header = ['UserName', 'BirthDay', 'Eligible', 'randomId', 'BizzFuzz']
	writer.writerow(header)
	for item in allUser:
		
		row = [item.username, item.birthday , oldRange(item.birthday) , item.randomId, checkBizzFuzz(item.randomId)]
		writer.writerow(row)

		#import pdb; pdb.set_trace()		
		#writer.writerow(item)
	
	return response

def updateUser(request, val):
	
	oldUser = User.objects.get(username=val)

	#oldUser.delete()

	form = UserForm(request.POST)
	
	if form.is_valid():

		oldUser.birthday = form.cleaned_data.get('birthday')
		oldUser.randomId = form.cleaned_data.get('randomId')	
		oldUser.username = form.cleaned_data.get('username')		
		oldUser.password = form.cleaned_data.get('password')
		#import pdb; pdb.set_trace()
		oldUser.save()
		# messages.add_message(request, messages.INFO, 'Successfully change the user!')	
		# messages.error = (request, "Hello World")
		# messages.add_message(request, messages.ERROR, 'Why wont')
	else:
		messages.warning(request, "Please input correct data")
		form = UserForm(request.POST)

	return redirect('list')


def deleteUser(request, val):
			
	u = User.objects.get(username=val)
	#import pdb; pdb.set_trace()
	u.delete()
	#message.success(request, "The user is deleted")
	
		#message.error(request, "User does not Exist")

	return redirect('list')

def createUser(request):

	if request.method == 'POST':		
		
		form = UserForm(request.POST)		
							
		if form.is_valid():

			user = User()
			
			user.birthday = form.cleaned_data.get('birthday')
			user.randomId = form.cleaned_data.get('randomId')	
			user.username = form.cleaned_data.get('username')		
			user.password = form.cleaned_data.get('password')							
			user.save()		
			#import pdb; pdb.set_trace()		
			# messages.success(request, 'Form submission successful')
			return redirect('list')
		else:
			form = UserForm(request.POST)
		
		return redirect('add')	
		

	



