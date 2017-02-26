from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from Users.models import User
from authentication.forms import SignUpForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if not form.is_valid():
			return render(request, 'signup.html',
						  {'form': form})

		else:
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')			
			birthday = form.cleaned_data.get('birthday')
			randomId = form.cleaned_data.get('randomId')

			User.objects.create_user(username=username, password=password,
									 email=email, randomId=randomId, birthday=birthday)
			#import pdb; pdb.set_trace()
			user = authenticate(username=username, password=password)
			login(request, user)
			welcome_post = '{0} has joined the network.'.format(user.username,
																user.username)
			
			return redirect('feeds')

	else:
		return render(request, 'signup.html',
					  {'form': SignUpForm()})
