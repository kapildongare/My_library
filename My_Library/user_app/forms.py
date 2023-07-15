from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User


class NewUserForm(UserCreationForm):  
	email = forms.EmailField(required=True)
	first_name = forms.CharField()
	last_name = forms.CharField()

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		print(user.__dict__)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		# user.is_staff = True   # in order to get the access for admin UI
		if commit:
			user.save() 
		return user