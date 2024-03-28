from django import forms
from .models import MenuItem
from djmoney.models.fields import MoneyField


class MenuItemForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
        'maxlength': '150',
    }))
    price = MoneyField()
    category = forms.ChoiceField(choices=MenuItem.CATEGORY_CHOICES)
    image = forms.ImageField()
    is_current = forms.BooleanField(required=False)

    class Meta:
        model = MenuItem
        fields = ['title', 'content', 'price', 'category', 'image',
                  'is_current']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.image.name = f"{instance.title.lower(
            ).replace(' ', '-')}.{instance.image.name.split('.')[-1]}"
        if commit:
            instance.save()
        return instance
