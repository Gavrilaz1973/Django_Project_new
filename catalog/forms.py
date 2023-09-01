from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']
        for i in range(len(forbidden_words)):
            if cleaned_data.lower() == forbidden_words[i]:
                raise forms.ValidationError('Запрещенный продукт')
        return cleaned_data

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        cleaned_data = self.cleaned_data['description']
        for i in range(len(forbidden_words)):
            if forbidden_words[i] in cleaned_data.lower():
                raise forms.ValidationError('Запрещенный продукт')
        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__' #('product', 'number_ver', 'name_ver',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # active_version = forms.BooleanField(required=False, label="Активная версия")


class ProductCuttedForm(forms.ModelForm):
    name = forms.CharField(max_length=100, disabled=True)
    # description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = forms.ImageField(disabled=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE)
    price = forms.IntegerField(disabled=True)
    # date_create = models.DateField(**NULLABLE, verbose_name='Дата создания', auto_now_add=True)
    # date_change = models.DateField(**NULLABLE, verbose_name='Дата изменения', auto_now=True)
    # owner = forms.ForeignKey(disabled=True)
    # is_published = models.BooleanField(verbose_name='Опубликовано', default=False)

    class Meta:
        model = Product
        exclude = ('owner',)



