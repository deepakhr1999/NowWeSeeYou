from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def register(request):
	context = {
		'uform' : UserRegistrationForm(),
		'pform'	: ProfileCreationForm(),
	}

	if request.method == 'POST':
		uform = UserRegistrationForm(request.POST)
		if uform.is_valid():
			user = uform.save()
			#now the user profile is also created, need to update their profile
			pform = ProfileCreationForm(request.POST, instance = user.profile)
			if pform.is_valid():	
				pform.save()
				messages.success(request, f'Account for {user.username}, {user.profile.rollno} has been created')
				return redirect('login')
			else:
				messages.info(request, 'pform not valid')

		else:
			messages.info(request, 'uform not valid')

	return render(request, 'user/register.html', context)