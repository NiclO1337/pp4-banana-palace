from django import forms
from .models import Table, Reservation
from datetime import date


class PickDateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': date.today()}), label="Select date:")

    class Meta:
        model = Table
        fields = ['date',]