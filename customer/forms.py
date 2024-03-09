from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Customer

class EditAccountForm(UserChangeForm):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone = PhoneNumberField()
    email = forms.EmailField(widget=forms.EmailInput)

