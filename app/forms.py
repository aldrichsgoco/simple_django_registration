from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your forms here.
"""
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CreateUser(ModelForm):
	username = forms.CharField(max_length=32, required=True)
	password = forms.CharField(max_length=32, required=True)
	class Meta:
		model = User
		fields = ['username', 'password']
"""
class SetEmail(ModelForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ['email',]

class SetFirstName(ModelForm):
	first_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ['first_name',]

class SetLastName(ModelForm):
	last_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ['last_name',]		
