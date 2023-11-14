from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

from app.models import Employee

class SignupForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email']
        labels = {'email':'Email'}
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class AddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','phone_no','address','image']
        labels = {'name':'Name','email':'Email','address':'Address','phone_no':'Phone Number','image':'Image'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
        }

class UserupdateForm(forms.ModelForm):
   
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
  
    class Meta:
        model = Employee
        fields = ['image', 'address']