from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('user', )

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        prohibited_data = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if cleaned_data.lower() in prohibited_data:
            raise forms.ValidationError('Вы пытаетесь загрузить запрещенные продукты!!!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        prohibited_data = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if cleaned_data.lower() in prohibited_data:
            raise forms.ValidationError('Вы пытаетесь загрузить запрещенные продукты!!!')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = ('number', 'name', 'is_active', 'product')
