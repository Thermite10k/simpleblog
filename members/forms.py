from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from theblog.models import Profile


class profile_page_form(forms.ModelForm):
	profile_pic = forms.ImageField(required = False)
	class Meta:
		model = Profile
		fields = ('bio' ,'profile_pic', 'website_url', 'facebook_url', 'instagram_url')
		widgets = {

		'bio': forms.Textarea(attrs={'class': 'form-control'}),

		#'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
		'website_url': forms.TextInput(attrs={'class': 'form-control'}),
		'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
		'instagram_url': forms.TextInput(attrs={'class': 'form-control'})}


class register_user_form(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

	'''class Meta:
					model = User
					fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
			
					widgets = {
			
					'username': forms.TextInput(attrs={'class':'form-control'}),
					'password1': forms.TextInput(attrs={'class':'form-control'}),
					'password2': forms.TextInput(attrs={'class':'form-control'}),
					}'''
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'	


class UpdateProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
			
	'''def __init__(self, *args, **kwargs):
					super(UserChangeForm,self).__init__(*args,**kwargs)
			
					self.fields['username'].widget.attrs['class'] = 'form-control'
					self.fields['first_name'].widget.attrs['class'] = 'form-control'
					self.fields['last_name'].widget.attrs['class'] = 'form-control'
					self.fields['email'].widget.attrs['class'] = 'form-control'''


class UpdateProfilePageForm(UserChangeForm):
	bio = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control"}))
	profile_pic = forms.ImageField(required = False)
	website_url = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}), required = False)
	facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required = False)
	instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}), required = False)
	class Meta:
		model = User
		fields = ('bio', 'website_url', 'facebook_url', 'instagram_url', 'profile_pic')


class PasswordChangingForm(PasswordChangeForm):


	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')
			
