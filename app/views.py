from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from .forms import SetEmail, SetFirstName, SetLastName

# Create your views here.
#def home(response):
#	return render(response, "app/home.html", {})

def log_in(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				if not request.user.email:
					return redirect(reverse('step_1'))
				if not request.user.first_name:
					return redirect(reverse('step_2'))
				if not request.user.last_name:
					return redirect(reverse('step_3'))
				return redirect(reverse('inside'))
			else:
				messages.error(request,"Invalid username or password.")
				return redirect(reverse('log_in'))
		else:
			messages.error(request,"Invalid username or password.")
			return redirect(reverse('log_in'))
	else:		
		form = AuthenticationForm()
		return render(request=request, template_name="app/log_in.html",context={"login_form":form})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(reverse('step_1'))
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
			return redirect(reverse('register'))
	else:
		form = UserCreationForm()
		return render(request=request, template_name="app/register.html", context={"register_form":form})

def step_1(request):
	if request.method == "POST":
		form = SetEmail(data=request.POST,instance=request.user)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect(reverse('step_2'))
		else:
			messages.error(request, "Not Valid")
			return redirect(reverse('step_1'))
	else:
		form = SetEmail(instance=request.user)
		if not request.user.email:
			form.initial['email'] = request.user.email
		return render(request=request, template_name="app/step_1.html", context={"set_email_form":form})

	#return render(response, "app/step_1.html", {})

def step_2(request):
	if request.method == "POST":
		form = SetFirstName(data=request.POST,instance=request.user)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect(reverse('step_3'))
		else:
			messages.error(request, "Not Valid")
			return redirect(reverse('step_2'))
	else:
		form = SetFirstName(instance=request.user)
		if not request.user.first_name:
			form.initial['first_name'] = request.user.first_name
		return render(request=request, template_name="app/step_2.html", context={"set_name_form":form})
	#return render(response, "app/step_2.html", {})

def step_3(request):
	if request.method == "POST":
		form = SetLastName(data=request.POST,instance=request.user)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect(reverse('inside'))
		else:
			messages.error(request, "Not Valid")
			return redirect(reverse('step_3'))
	else:
		form = SetLastName(instance=request.user)
		if not request.user.last_name:
			form.initial['last_name'] = request.user.last_name
		return render(request=request, template_name="app/step_3.html", context={"set_name_form":form})
	#return render(response, "app/step_3.html", {})

def inside(request):
	return render(request, "app/inside.html", {"curr_user":request})

def log_out(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect(reverse('register'))	