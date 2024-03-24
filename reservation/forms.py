from django import forms
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
    time = forms.ChoiceField(choices=Reservation.TIME_CHOISES,
                             label="Time of arrival:")
    party_size = forms.ChoiceField(choices=Reservation.PARTY_SIZE,
                                   label="Party size:")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.table = kwargs.pop('table', None)
        super(ReserveTableForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):

        user = self.request.user

        table = self.table

        reservation = Reservation(
            user=user,
            time=self.cleaned_data['time'],
            party_size=self.cleaned_data['party_size'],
            table=table,
        )
        if commit:
            reservation.save()
        return reservation

    class Meta:
        model = Reservation
        fields = ['time', 'party_size',]