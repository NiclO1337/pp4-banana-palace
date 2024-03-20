from django import forms
from django.contrib.auth.models import User
from customer.models import Customer
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
    first_name = forms.CharField(max_length=20, label="First name:")
    last_name = forms.CharField(max_length=30, label="Last name:")
    phone = PhoneNumberField(label="Phone number:")
    time = forms.ChoiceField(choices=Reservation.TIME_CHOISES,
                             label="Time of arrival:")
    party_size = forms.ChoiceField(choices=Reservation.PARTY_SIZE,
                                   label="Party size:")

    def save(self, commit=True):
        first_name = User.objects.get(
            first_name=self.cleaned_data['first_name'])
        last_name = User.objects.get(
            last_name=self.cleaned_data['last_name'])
        phone = User.objects.get(customer__phone=self.cleaned_data['phone'])
        reservation = Reservation(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            time=self.cleaned_data['time'],
            party_size=self.cleaned_data['party_size'],
        )
        if commit:
            reservation.save()
        return reservation

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'phone', 'time', 'party_size',]