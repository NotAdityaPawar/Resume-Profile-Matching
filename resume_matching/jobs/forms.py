from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Job

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class AddJob(forms.ModelForm):
    class Meta:
        model= Job
        #fields = ["title","body","location"]
        fields = '__all__'

class DeleteJob(forms.ModelForm):
    pass