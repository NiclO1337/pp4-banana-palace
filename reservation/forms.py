from django.contrib.auth.models import User
from django import forms
from .models import Table, Reservation


class PickDateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Table
        fields = ('date',)