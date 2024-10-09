# Generated by Django 5.1.1 on 2024-10-09 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter_app', '0002_alter_menshirt_options_alter_menshoes_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertionTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=20)),
                ('input_measure', models.CharField(blank=True, max_length=20)),
                ('input_size', models.CharField(blank=True, max_length=20)),
                ('output_measure', models.CharField(blank=True, max_length=20)),
                ('output_size', models.CharField(blank=True, max_length=20)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
