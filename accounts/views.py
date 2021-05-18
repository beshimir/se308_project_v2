





from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(login_url='login')
def home(request):
	return render(request, 'accounts/customlanding.html', {'all':UserProfile.objects.all})

@login_required(login_url='login')
def hman(request):
	return render(request, 'accounts/hmanlanding.html')

@login_required(login_url='login')
def admin(request):
	return HttpResponseRedirect('admin/')



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			uname = request.POST.get('username')
			pword = request.POST.get('password')

			u = authenticate(request, username=uname, password=pword)

			if u is not None:
				login(request, u)
					
				all_members = UserProfile.objects.all

				for item in UserProfile.objects.all():

					if (item.user.username == uname) and (item.typeOfProfile == 'Customer'):
						
						return render(request, 'accounts/customlanding.html', {'all':all_members})
					else:
						
						return render(request, 'accounts/hmanlanding.html', {'all':all_members})
					
			else:
				messages.info(request, 'Username or password is incorrect.')


	context = {}
	return render(request, 'accounts/login.html', context)



def logoutPage(request):
	logout(request)
	return redirect('login')

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm();

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			profile_form = UserProfileForm(request.POST)
			if form.is_valid() and profile_form.is_valid():

				user = form.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				profile.save()

				uname = form.cleaned_data.get('username')
				messages.success(request, 'Account successfully created for ' + uname)
				return redirect('login')
			novalidate = True
		else:
			form = CreateUserForm()
			profile_form = UserProfileForm()


	context = {'form':form, 'profile_form':profile_form}
	return render(request, 'accounts/register.html', context)

