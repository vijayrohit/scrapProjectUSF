from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, PasswordInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=TextInput(attrs={'class':'validate','placeholder': 'School Email ID'}))
    password1 = forms.PasswordInput(attrs={'placeholder': 'Password'})
    password2 = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email address is already in use. Please go ahead and login using it.')
        if not email.endswith('.edu'):
            raise forms.ValidationError(u'Please use your school issued Email ID, which ends with .edu')
        return email