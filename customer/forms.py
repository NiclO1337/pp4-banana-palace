from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Customer

class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


class EditUserFormReservation(forms.ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="First name:")
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="Last name:")

    class Meta:
        model = User
        fields = ['first_name', 'last_name',]


class EditCustomerForm(forms.ModelForm):
    phone = PhoneNumberField(label="Phone number:")

    class Meta:
        model = Customer
        fields = ['phone',]