from django import forms
from .models import Menu
from djmoney.models.fields import MoneyField


class MenuItemForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
        'maxlength': '150',
    }))
    price = MoneyField()
    category = forms.ChoiceField(choices=Menu.CATEGORY_CHOICES)
    image = forms.ImageField()
    is_current = forms.BooleanField


    class Meta:
        model = Menu
        fields = ['title', 'content', 'price', 'category', 'image',
                  'is_current']