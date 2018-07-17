from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', 
		max_length=30,
		widget=forms.TextInput(attrs={'size':32, 'class':'form-control'}))
	email = forms.EmailField(label='Email',
		widget=forms.TextInput(attrs={'size':32, 'class':'form-control'}))
	password1 = forms.CharField(
		label='Password',
		widget=forms.PasswordInput(attrs={'size':32, 'class':'form-control'})
	)
	password2 = forms.CharField(
		label='Confirm Password',
		widget=forms.PasswordInput(attrs={'size':32, 'class':'form-control'})
	)

#Password Validation
def clean_password2(self):
	if 'password1' in self.clean_data:
		password1 = self.clean_data['password1']
		password2 = self.clean_data['password2']
		if password1 != password2:
			raise forms.ValidationError('Passwords do not match!')

#Username Validation
def clean_username(self):
	username =  self.clean_data['username']
	if not re.search(r'^\w+$', username):
		raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken!')

class BookmarkSaveForm(forms.Form):
	url = forms.URLField(
	label='URL',
	widget=forms.TextInput(attrs={'size': 64})
	)
	title = forms.CharField(
	label='Title',
	widget=forms.TextInput(attrs={'size': 64})
	)
	tags = forms.CharField(
	label='Tags',
	required=False,
	widget=forms.TextInput(attrs={'size': 64})
	)
	share = forms.BooleanField(
		label='Share on the main page',
		required= False
	)
#Search Form
class SearchForm(forms.Form):
	query = forms.CharField(
		label='Enter a keyword to search for',
		widget=forms.TextInput(attrs={'size':32, 'class':'form-control'})
	)

class FriendInviteForm(forms.Form):  
	name = forms.CharField(
		label='Friend\'s Name',
		widget=forms.TextInput(attrs={'size':32, 'class':'form-control'})
		)  
	email = forms.EmailField(
		label='Friend\'s Email',
		widget=forms.TextInput(attrs={'size':32, 'class':'form-control'})
		)  