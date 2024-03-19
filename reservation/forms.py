from django import forms
from django.contrib.auth.models import User
from .models import Table, Reservation
from datetime import date
from phonenumber_field.formfields import PhoneNumberField


class PickDateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': date.today()}), label="Select date:")

    class Meta:
        model = Table
        fields = ['date',]


class ReserveTableForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    phone = PhoneNumberField()
    time = forms.TimeField()
    party_size = forms.ChoiceField(choices=Reservation.PARTY_SIZE)

    def save(self, commit=True):
        user = User.objects.get(username=self.cleaned_data['username'])
        customer = User.customer.objects.get(phone=self.cleaned_data['phone'])
        reservation = Reservation(
            user=user,
            customer=user.customer,
            time=self.cleaned_data['time'],
            party_size=self.cleaned_data['party_size'],
        )
        if commit:
            reservation.save()
        return reservation

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'phone', 'time', 'party_size',]