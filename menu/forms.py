from django import forms
from .models import MenuItem
from djmoney.models.fields import MoneyField


class MenuItemForm(forms.ModelForm):
    """
    Form for creating and updating MenuItem instances.

    **save method:**
    - Customizes the save method to handle image
    naming based on the menu item's title.
    """
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
        if self.cleaned_data.get('image'):
            instance.image.name = f'{instance.title.lower().replace(
                ' ', '-').replace('&', 'and')}.{instance.image.name.split(
                    '.')[-1]}'
        else:
            instance.image = self.instance.image
        if commit:
            instance.save()
        return instance
