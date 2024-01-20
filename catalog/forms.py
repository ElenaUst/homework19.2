from django import forms

from catalog.models import Product, Version


class StyleMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            try:
                input_type = field.widget.input_type
                if input_type == 'checkbox':
                    field.widget.attrs['class'] = 'form-check'
                else:
                    field.widget.attrs['class'] = 'form-control'
            except AttributeError:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin):
    prohibited_data = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Product
        exclude = ('user', 'create_date', 'last_change_date',)

    def clean_name(self):
        prohibited_data = self.prohibited_data
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data.lower() in prohibited_data:
            raise forms.ValidationError('Вы пытаетесь загрузить запрещенные продукты!!!')
        return cleaned_data

    def clean_description(self):
        prohibited_data = self.prohibited_data
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data.lower() in prohibited_data:
            raise forms.ValidationError('Вы пытаетесь загрузить запрещенные продукты!!!')
        return cleaned_data


class VersionForm(StyleMixin):

    class Meta:
        model = Version
        fields = ('number', 'name', 'is_active', 'product')


class ModeratorProductForm(ProductForm):

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
