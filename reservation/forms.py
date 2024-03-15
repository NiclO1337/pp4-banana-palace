from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Table, Reservation
from datetime import datetime, date


class PickDateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Table
        fields = ('date',)