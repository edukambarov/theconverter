from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from users.models import User

class ConvertionTracker(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=True)
    input_measure = models.CharField(max_length=50, blank=True)
    input_size = models.CharField(max_length=50, blank=True)
    output_measure = models.CharField(max_length=50, blank=True)
    output_size = models.CharField(max_length=50, blank=True)



class MenShoes(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    eur = models.CharField(max_length=20, blank=True, verbose_name='Европа')
    uk = models.CharField(max_length=20, blank=True, verbose_name='Великобритания')
    usa = models.CharField(max_length=20, blank=True, verbose_name='США')
    jap = models.CharField(max_length=20, blank=True, verbose_name='Япония')
    cm = models.CharField(max_length=20, blank=True, verbose_name='Длина стопы (см)')

    class Meta:
        verbose_name = "Мужская обувь"


class WomenShoes(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    eur = models.CharField(max_length=20, blank=True, verbose_name='Европа')
    uk = models.CharField(max_length=20, blank=True, verbose_name='Великобритания')
    usa = models.CharField(max_length=20, blank=True, verbose_name='США')
    jap = models.CharField(max_length=20, blank=True, verbose_name='Япония')
    cm = models.CharField(max_length=20, blank=True, verbose_name='Длина стопы (см)')

    class Meta:
        verbose_name = "Женская обувь"



class WomenTShirt(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    eur = models.CharField(max_length=20, blank=True, verbose_name='Европа')
    uk_usa = models.CharField(max_length=20, blank=True, verbose_name='США/Великобритания')
    inter = models.CharField(max_length=20, blank=True, verbose_name='Международный')
    height_cm = models.CharField(max_length=20, blank=True, verbose_name='Рост (см)')

    class Meta:
        verbose_name = "Женские футболки"


class MenTShirt(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    eur = models.CharField(max_length=20, blank=True, verbose_name='Европа')
    uk_usa = models.CharField(max_length=20, blank=True, verbose_name='США/Великобритания')
    inter = models.CharField(max_length=20, blank=True, verbose_name='Международный')
    height_cm = models.CharField(max_length=20, blank=True, verbose_name='Рост (см)')

    class Meta:
        verbose_name = "Мужские футболки"


class MenTrousers(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    eur = models.CharField(max_length=20, blank=True, verbose_name='Европа')
    uk_usa = models.CharField(max_length=20, blank=True, verbose_name='США/Великобритания')
    inter = models.CharField(max_length=20, blank=True, verbose_name='Международный')
    height_cm = models.CharField(max_length=20, blank=True, verbose_name='Рост (см)')

    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    ita = models.CharField(max_length=20, blank=True, verbose_name='Италия')
    fra = models.CharField(max_length=20, blank=True, verbose_name='Франция')
    usa = models.CharField(max_length=20, blank=True, verbose_name='США')
    inter = models.CharField(max_length=20, blank=True, verbose_name='Международный')
    waist_cm = models.CharField(max_length=20, blank=True, verbose_name='Обхват бёдер (см)')
    jeans_waist = models.CharField(max_length=20, blank=True, verbose_name='Размер джинсов (W)')

    class Meta:
        verbose_name = "Мужские брюки/джинсы"

class WomenTrousers(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    ita = models.CharField(max_length=20, blank=True, verbose_name='Италия')
    fra = models.CharField(max_length=20, blank=True, verbose_name='Франция')
    uk = models.CharField(max_length=20, blank=True, verbose_name='Великобритания')
    usa = models.CharField(max_length=20, blank=True, verbose_name='США')
    jap = models.CharField(max_length=20, blank=True, verbose_name='Япония')
    inter = models.CharField(max_length=20, blank=True, verbose_name='Международный')
    hips_cm = models.CharField(max_length=20, blank=True, verbose_name='Обхват бёдер (см)')
    waist_cm = models.CharField(max_length=20, blank=True, verbose_name='Обхват талии (см)')
    jeans_waist = models.CharField(max_length=20, blank=True, verbose_name='Размер джинсов (W)')

    class Meta:
        verbose_name = "Женские брюки/джинсы"


class MenShirt(models.Model):
    # category = models.ForeignKey(Category)
    rus_eur = models.CharField(max_length=20, blank=True)
    uk_usa = models.CharField(max_length=20, blank=True)
    inter = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Мужские рубашки"


class WomenDressBlouse(models.Model):
    # category = models.ForeignKey(Category)
    rus = models.CharField(max_length=20, blank=True, verbose_name='Россия')
    uk = models.CharField(max_length=20, blank=True, verbose_name='Великобритания')
    ger = models.CharField(max_length=20, blank=True, verbose_name='Германия')
    ita = models.CharField(max_length=20, blank=True, verbose_name='Италия')
    fra = models.CharField(max_length=20, blank=True, verbose_name='Франция')
    usa = models.CharField(max_length=20, blank=True, verbose_name='США')
    inter = models.CharField(max_length=20, blank=True, verbose_name='Международный')

    class Meta:
        verbose_name = "Женские платья/блузки"




