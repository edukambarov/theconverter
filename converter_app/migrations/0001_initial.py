# Generated by Django 5.1.1 on 2024-10-07 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenShirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus_eur', models.CharField(blank=True, max_length=20)),
                ('uk_usa', models.CharField(blank=True, max_length=20)),
                ('inter', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenShoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('eur', models.CharField(blank=True, max_length=20)),
                ('uk', models.CharField(blank=True, max_length=20)),
                ('usa', models.CharField(blank=True, max_length=20)),
                ('jap', models.CharField(blank=True, max_length=20)),
                ('cm', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenTrousers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('ita', models.CharField(blank=True, max_length=20)),
                ('fra', models.CharField(blank=True, max_length=20)),
                ('usa', models.CharField(blank=True, max_length=20)),
                ('inter', models.CharField(blank=True, max_length=20)),
                ('waist_cm', models.CharField(blank=True, max_length=20)),
                ('jeans_waist', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenTShirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('eur', models.CharField(blank=True, max_length=20)),
                ('uk_usa', models.CharField(blank=True, max_length=20)),
                ('inter', models.CharField(blank=True, max_length=20)),
                ('height_cm', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WomenDressBlouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('uk', models.CharField(blank=True, max_length=20)),
                ('ger', models.CharField(blank=True, max_length=20)),
                ('ita', models.CharField(blank=True, max_length=20)),
                ('fra', models.CharField(blank=True, max_length=20)),
                ('usa', models.CharField(blank=True, max_length=20)),
                ('inter', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WomenShoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('eur', models.CharField(blank=True, max_length=20)),
                ('uk', models.CharField(blank=True, max_length=20)),
                ('usa', models.CharField(blank=True, max_length=20)),
                ('jap', models.CharField(blank=True, max_length=20)),
                ('cm', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WomenTrousers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('ita', models.CharField(blank=True, max_length=20)),
                ('fra', models.CharField(blank=True, max_length=20)),
                ('uk', models.CharField(blank=True, max_length=20)),
                ('usa', models.CharField(blank=True, max_length=20)),
                ('jap', models.CharField(blank=True, max_length=20)),
                ('inter', models.CharField(blank=True, max_length=20)),
                ('waist_cm', models.CharField(blank=True, max_length=20)),
                ('hips_cm', models.CharField(blank=True, max_length=20)),
                ('jeans_waist', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WomenTShirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus', models.CharField(blank=True, max_length=20)),
                ('eur', models.CharField(blank=True, max_length=20)),
                ('uk_usa', models.CharField(blank=True, max_length=20)),
                ('inter', models.CharField(blank=True, max_length=20)),
                ('height_cm', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Converter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.PositiveIntegerField()),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
