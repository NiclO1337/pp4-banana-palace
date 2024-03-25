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
    notes = forms.CharField(label="Notes or special requests:",
                            widget=forms.Textarea(attrs={
                                'rows': '3',
                                'maxlength': '200',
                            }))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.table = kwargs.pop('table', None)
        super(ReserveTableForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):

        if self.instance:

            if self.instance.table is not None:

                self.instance.table.reserved = False
                self.instance.table.save()

            self.instance.time = self.cleaned_data['time']
            self.instance.party_size = self.cleaned_data['party_size']
            self.instance.table = self.table
            if commit:
                self.instance.save()

            if self.table is not None:
                self.table.reserved = True
                self.table.save()

            return self.instance

        else:

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
        fields = ['time', 'party_size', 'notes',]