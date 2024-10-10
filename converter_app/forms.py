from django import forms
from django.apps import apps
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.forms import RadioSelect


from .models import *

class SelectCategoryForm(forms.Form):
    app_models = apps.get_app_config('converter_app').get_models()
    MODELS = [(model.__name__, model._meta.verbose_name.title()) for model in app_models if not model.__name__ =='ConvertionTracker']

    chosen_category = forms.ChoiceField(widget=RadioSelect,
                                        choices=MODELS,
                                        label='Выберите категорию ')

class MenShoesForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in MenShoes._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                        label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(MenShoesForm, self).__init__(*args, **kwargs)
        #Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]
    def clean(self):
        cleaned_data = super(MenShoesForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(MenShoes.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'eur':
            input_size_choices= [(x, x) for x in list(MenShoes.objects.all().values_list('eur', flat=True))]
        elif input_measure == 'uk':
            input_size_choices = [(x, x) for x in list(MenShoes.objects.all().values_list('uk', flat=True))]
        elif input_measure == 'usa':
            input_size_choices = [(x, x) for x in list(MenShoes.objects.all().values_list('usa', flat=True))]
        elif input_measure == 'jap':
            input_size_choices = [(x, x) for x in list(MenShoes.objects.all().values_list('jap', flat=True))]
        elif input_measure == 'cm':
            input_size_choices = [(x, x) for x in list(MenShoes.objects.all().values_list('cm', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data


class WomenShoesForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in WomenShoes._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(WomenShoesForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(WomenShoesForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(WomenShoes.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'eur':
            input_size_choices = [(x, x) for x in list(WomenShoes.objects.all().values_list('eur', flat=True))]
        elif input_measure == 'uk':
            input_size_choices = [(x, x) for x in list(WomenShoes.objects.all().values_list('uk', flat=True))]
        elif input_measure == 'usa':
            input_size_choices = [(x, x) for x in list(WomenShoes.objects.all().values_list('usa', flat=True))]
        elif input_measure == 'jap':
            input_size_choices = [(x, x) for x in list(WomenShoes.objects.all().values_list('jap', flat=True))]
        elif input_measure == 'cm':
            input_size_choices = [(x, x) for x in list(WomenShoes.objects.all().values_list('cm', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data


class WomenTShirtForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in WomenTShirt._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(WomenTShirtForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(WomenTShirtForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(WomenTShirt.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'eur':
            input_size_choices = [(x, x) for x in list(WomenTShirt.objects.all().values_list('eur', flat=True))]
        elif input_measure == 'uk_usa':
            input_size_choices = [(x, x) for x in list(WomenTShirt.objects.all().values_list('uk_usa', flat=True))]
        elif input_measure == 'inter':
            input_size_choices = [(x, x) for x in list(WomenTShirt.objects.all().values_list('inter', flat=True))]
        elif input_measure == 'height_cm':
            input_size_choices = [(x, x) for x in list(WomenTShirt.objects.all().values_list('height_cm', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data




class MenTShirtForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in MenTShirt._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(MenTShirtForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(MenTShirtForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(MenTShirt.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'eur':
            input_size_choices = [(x, x) for x in list(MenTShirt.objects.all().values_list('eur', flat=True))]
        elif input_measure == 'uk_usa':
            input_size_choices = [(x, x) for x in list(MenTShirt.objects.all().values_list('uk_usa', flat=True))]
        elif input_measure == 'inter':
            input_size_choices = [(x, x) for x in list(MenTShirt.objects.all().values_list('inter', flat=True))]
        elif input_measure == 'height_cm':
            input_size_choices = [(x, x) for x in list(MenTShirt.objects.all().values_list('height_cm', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data


class MenTrousersForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in MenTrousers._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(MenTrousersForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(MenTrousersForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'ita':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('ita', flat=True))]
        elif input_measure == 'fra':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('fra', flat=True))]
        elif input_measure == 'usa':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('usa', flat=True))]
        elif input_measure == 'inter':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('inter', flat=True))]
        elif input_measure == 'waist_cm':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('waist_cm', flat=True))]
        elif input_measure == 'jeans_waist':
            input_size_choices = [(x, x) for x in list(MenTrousers.objects.all().values_list('jeans_waist', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data



class WomenTrousersForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in WomenTrousers._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(WomenTrousersForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(WomenTrousersForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'ita':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('ita', flat=True))]
        elif input_measure == 'fra':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('fra', flat=True))]
        elif input_measure == 'usa':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('usa', flat=True))]
        elif input_measure == 'uk':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('uk', flat=True))]
        elif input_measure == 'jap':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('jap', flat=True))]
        elif input_measure == 'inter':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('inter', flat=True))]
        elif input_measure == 'waist_cm':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('waist_cm', flat=True))]
        elif input_measure == 'jeans_waist':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('jeans_waist', flat=True))]
        elif input_measure == 'hips_cm':
            input_size_choices = [(x, x) for x in list(WomenTrousers.objects.all().values_list('hips_cm', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data


class MenShirtForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in MenShirt._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(MenShirtForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(MenShirtForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus_eur':
            input_size_choices = [(x, x) for x in list(MenShirt.objects.all().values_list('rus_eur', flat=True))]
        elif input_measure == 'uk_usa':
            input_size_choices = [(x, x) for x in list(MenShirt.objects.all().values_list('uk_usa', flat=True))]
        elif input_measure == 'inter':
            input_size_choices = [(x, x) for x in list(MenShirt.objects.all().values_list('inter', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data


class WomenDressBlouseForm(forms.Form):
    input_measure_choices = [(x.name, x.verbose_name.title())
                             for x in WomenDressBlouse._meta.get_fields()][1:]
    output_measure = forms.ChoiceField(widget=RadioSelect,
                                       choices=input_measure_choices,
                                       label='Выберите желаемую систему измерения (или страну, в системе измерения которой вам нужен размер :')
    input_measure = forms.ChoiceField(widget=RadioSelect,
                                      choices=input_measure_choices,
                                      label='Выберите известную вам систему измерения (или страну, в измерения системе которой вам известен размер) ')
    input_size = forms.ChoiceField(widget=RadioSelect,
                                   label='Выберите размер ')

    def __init__(self, *args, **kwargs):
        super(WomenDressBlouseForm, self).__init__(*args, **kwargs)
        # Добавляем заглушку для выбора в поле, которое будем чистить в clean()
        self.fields['input_size'].choices = [('', '---------')]

    def clean(self):
        cleaned_data = super(WomenDressBlouseForm, self).clean()
        input_measure = cleaned_data.get('input_measure')
        if input_measure == 'rus':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('rus', flat=True))]
        elif input_measure == 'ita':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('ita', flat=True))]
        elif input_measure == 'fra':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('fra', flat=True))]
        elif input_measure == 'usa':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('usa', flat=True))]
        elif input_measure == 'ger':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('ger', flat=True))]
        elif input_measure == 'uk':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('uk', flat=True))]
        elif input_measure == 'inter':
            input_size_choices = [(x, x) for x in list(WomenDressBlouse.objects.all().values_list('inter', flat=True))]
        else:
            input_size_choices = []
        self.fields['input_size'].choices = input_size_choices
        return cleaned_data