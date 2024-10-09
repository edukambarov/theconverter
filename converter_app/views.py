from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import *
from .forms import SelectCategoryForm, MenShoesForm, WomenShoesForm, WomenTShirtForm, MenTShirtForm, MenTrousersForm, \
    WomenTrousersForm, MenShirtForm, WomenDressBlouseForm
from users.models import User


def index(request):
    return render(request, 'home.html')

@login_required
def show_searches(request):
    your_searches = ConvertionTracker.objects.filter(person=request.user).order_by('-id')[:3]
    data = {'searches': your_searches}
    return render(request, 'profile.html', context=data)

@login_required
def select_category(request):

    submitbutton = request.POST.get("submit")
    chosen_category = ''
    chosen_category_title = ''
    form = SelectCategoryForm(request.POST or None)
    if form.is_valid():
        chosen_category = form.cleaned_data['chosen_category']
        chosen_category_title = [x[1] for x in list(form.fields['chosen_category'].choices)
                                 if x[0] == chosen_category][0]
    context = {'form': form,
               'chosen_category': chosen_category,
               'chosen_category_title': chosen_category_title,
               'submitbutton': submitbutton,
               }
    return render(request, "category.html", context)

@login_required
def men_shoes(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = MenShoesForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']
        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = MenShoes.objects.filter(rus=input_size).first()
        elif input_measure == 'uk':
            answer_item = MenShoes.objects.filter(uk=input_size).first()
        elif input_measure == 'usa':
            answer_item = MenShoes.objects.filter(usa=input_size).first()
        elif input_measure == 'jap':
            answer_item = MenShoes.objects.filter(jap=input_size).first()
        elif input_measure == 'eur':
            answer_item = MenShoes.objects.filter(eur=input_size).first()
        else:
            answer_item = MenShoes.objects.filter(cm=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'uk':
            output_size = answer_item.uk
        elif output_measure == 'usa':
            output_size = answer_item.usa
        elif output_measure == 'jap':
            output_size = answer_item.jap
        elif output_measure == 'eur':
            output_size = answer_item.eur
        else:
            output_size = answer_item.cm
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                                 if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                                 if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
               'submitbutton': submitbutton,
               'output_measure': output_measure,
               'output_size': output_size,
               }
    return render(request, "result.html", context)

@login_required
def women_shoes(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = WomenShoesForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = WomenShoes.objects.filter(rus=input_size).first()
        elif input_measure == 'uk':
            answer_item = WomenShoes.objects.filter(uk=input_size).first()
        elif input_measure == 'usa':
            answer_item = WomenShoes.objects.filter(usa=input_size).first()
        elif input_measure == 'jap':
            answer_item = WomenShoes.objects.filter(jap=input_size).first()
        elif input_measure == 'eur':
            answer_item = WomenShoes.objects.filter(eur=input_size).first()
        else:
            answer_item = WomenShoes.objects.filter(cm=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'uk':
            output_size = answer_item.uk
        elif output_measure == 'usa':
            output_size = answer_item.usa
        elif output_measure == 'jap':
            output_size = answer_item.jap
        elif output_measure == 'eur':
            output_size = answer_item.eur
        else:
            output_size = answer_item.cm
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
               'submitbutton': submitbutton,
               'output_measure': output_measure,
               'output_size': output_size,
               }
    return render(request, "result.html", context)

@login_required
def women_t_shirt(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = WomenTShirtForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = WomenTShirt.objects.filter(rus=input_size).first()
        elif input_measure == 'inter':
            answer_item = WomenTShirt.objects.filter(inter=input_size).first()
        elif input_measure == 'uk_usa':
            answer_item = WomenTShirt.objects.filter(uk_usa=input_size).first()
        elif input_measure == 'eur':
            answer_item = WomenTShirt.objects.filter(eur=input_size).first()
        else:
            answer_item = WomenTShirt.objects.filter(height_cm=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'inter':
            output_size = answer_item.inter
        elif output_measure == 'uk_usa':
            output_size = answer_item.uk_usa
        elif output_measure == 'eur':
            output_size = answer_item.eur
        else:
            output_size = answer_item.height_cm
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
               'submitbutton': submitbutton,
               'output_measure': output_measure,
               'output_size': output_size,
               }
    return render(request, "result.html", context)

@login_required
def men_t_shirt(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = MenTShirtForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = MenTShirt.objects.filter(rus=input_size).first()
        elif input_measure == 'inter':
            answer_item = MenTShirt.objects.filter(inter=input_size).first()
        elif input_measure == 'uk_usa':
            answer_item = MenTShirt.objects.filter(uk_usa=input_size).first()
        elif input_measure == 'eur':
            answer_item = MenTShirt.objects.filter(eur=input_size).first()
        else:
            answer_item = MenTShirt.objects.filter(height_cm=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'inter':
            output_size = answer_item.inter
        elif output_measure == 'uk_usa':
            output_size = answer_item.uk_usa
        elif output_measure == 'eur':
            output_size = answer_item.eur
        else:
            output_size = answer_item.height_cm
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
               'submitbutton': submitbutton,
               'output_measure': output_measure,
               'output_size': output_size,
               }
    return render(request, "result.html", context)

@login_required
def men_trousers(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = MenTrousersForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = MenTrousers.objects.filter(rus=input_size).first()
        elif input_measure == 'inter':
            answer_item = MenTrousers.objects.filter(inter=input_size).first()
        elif input_measure == 'usa':
            answer_item = MenTrousers.objects.filter(usa=input_size).first()
        elif input_measure == 'ita':
            answer_item = MenTrousers.objects.filter(ita=input_size).first()
        elif input_measure == 'fra':
            answer_item = MenTrousers.objects.filter(fra=input_size).first()
        elif input_measure == 'waist_cm':
            answer_item = MenTrousers.objects.filter(waist_cm=input_size).first()
        else:
            answer_item = MenTrousers.objects.filter(jeans_waist=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'inter':
            output_size = answer_item.inter
        elif output_measure == 'usa':
            output_size = answer_item.usa
        elif output_measure == 'ita':
            output_size = answer_item.ita
        elif output_measure == 'fra':
            output_size = answer_item.eur
        elif output_measure == 'waist_cm':
            output_size = answer_item.waist_cm
        else:
            output_size = answer_item.jeans_waist
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
                'submitbutton': submitbutton,
                'output_measure': output_measure,
                'output_size': output_size,
                }
    return render(request, "result.html", context)



@login_required
def women_trousers(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = WomenTrousersForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = WomenTrousers.objects.filter(rus=input_size).first()
        elif input_measure == 'inter':
            answer_item = WomenTrousers.objects.filter(inter=input_size).first()
        elif input_measure == 'usa':
            answer_item = WomenTrousers.objects.filter(usa=input_size).first()
        elif input_measure == 'uk':
             answer_item = WomenTrousers.objects.filter(uk=input_size).first()
        elif input_measure == 'jap':
            answer_item = WomenTrousers.objects.filter(jap=input_size).first()
        elif input_measure == 'ita':
            answer_item = WomenTrousers.objects.filter(ita=input_size).first()
        elif input_measure == 'fra':
            answer_item = WomenTrousers.objects.filter(fra=input_size).first()
        elif input_measure == 'hips_cm':
            answer_item = WomenTrousers.objects.filter(hips_cm=input_size).first()
        elif input_measure == 'waist_cm':
            answer_item = WomenTrousers.objects.filter(waist_cm=input_size).first()
        else:
            answer_item = WomenTrousers.objects.filter(jeans_waist=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'inter':
            output_size = answer_item.inter
        elif output_measure == 'usa':
            output_size = answer_item.usa
        elif output_measure == 'uk':
            output_size = answer_item.uk
        elif output_measure == 'ita':
            output_size = answer_item.ita
        elif output_measure == 'jap':
            output_size = answer_item.jap
        elif output_measure == 'fra':
            output_size = answer_item.eur
        elif output_measure == 'waist_cm':
            output_size = answer_item.waist_cm
        elif output_measure == 'hips_cm':
            output_size = answer_item.hips_cm
        else:
            output_size = answer_item.jeans_waist
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
                'submitbutton': submitbutton,
                'output_measure': output_measure,
                'output_size': output_size,
                }
    return render(request, "result.html", context)

@login_required
def men_shirt(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = MenShirtForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'uk_usa':
            answer_item = MenShirt.objects.filter(uk_usa=input_size).first()
        elif input_measure == 'rus_eur':
            answer_item = MenShirt.objects.filter(rus_eur=input_size).first()
        else:
            answer_item = MenShirt.objects.filter(inter=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus_eur':
            output_size = answer_item.rus_eur
        elif output_measure == 'uk_usa':
            output_size = answer_item.uk_usa
        else:
            output_size = answer_item.inter
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
                'submitbutton': submitbutton,
                'output_measure': output_measure,
                'output_size': output_size,
                }
    return render(request, "result.html", context)

@login_required
def women_dress_blouse(request):
    submitbutton = request.POST.get("submit")
    person = request.user
    input_measure = ''
    input_size = ''
    output_measure = ''
    output_size = ''
    form = WomenDressBlouseForm(request.POST or None)
    input_size = request.POST.get('input_size')
    form.fields['input_size'].choices = [(input_size, input_size)]
    if form.is_valid():
        output_measure = form.cleaned_data['output_measure']
        input_measure = form.cleaned_data['input_measure']
        input_size = form.cleaned_data['input_size']

        # Фильтруем объекты классы из БД, находим нужную строку
        if input_measure == 'rus':
            answer_item = WomenDressBlouse.objects.filter(rus=input_size).first()
        elif input_measure == 'inter':
            answer_item = WomenDressBlouse.objects.filter(inter=input_size).first()
        elif input_measure == 'usa':
            answer_item = WomenDressBlouse.objects.filter(usa=input_size).first()
        elif input_measure == 'uk':
             answer_item = WomenDressBlouse.objects.filter(uk=input_size).first()
        elif input_measure == 'jap':
            answer_item = WomenDressBlouse.objects.filter(jap=input_size).first()
        elif input_measure == 'ita':
            answer_item = WomenDressBlouse.objects.filter(ita=input_size).first()
        elif input_measure == 'fra':
            answer_item = WomenDressBlouse.objects.filter(fra=input_size).first()
        # Получаем искомый атрибут
        if output_measure == 'rus':
            output_size = answer_item.rus
        elif output_measure == 'inter':
            output_size = answer_item.inter
        elif output_measure == 'usa':
            output_size = answer_item.usa
        elif output_measure == 'uk':
            output_size = answer_item.uk
        elif output_measure == 'ita':
            output_size = answer_item.ita
        elif output_measure == 'jap':
            output_size = answer_item.jap
        elif output_measure == 'fra':
            output_size = answer_item.eur
        # Создаём объект трекера и сохраняем его
        new_search = ConvertionTracker(
            person=person,
            category=answer_item.__class__._meta.verbose_name.title(),
            input_measure=[x[1] for x in list(form.fields['input_measure'].choices)
                           if x[0] == input_measure][0],
            input_size=input_size,
            output_measure=[x[1] for x in list(form.fields['output_measure'].choices)
                            if x[0] == output_measure][0],
            output_size=output_size)
        new_search.save()
    context = {'form': form,
                'submitbutton': submitbutton,
                'output_measure': output_measure,
                'output_size': output_size,
                }
    return render(request, "result.html", context)
