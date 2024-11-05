from django.apps import apps
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
import csv


from converter_app.models import *


class Command(BaseCommand):
    help = "Create category"

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='the name of file to export tracker data')


    def handle(self, *args, **kwargs):
        filename = kwargs.get('filename')
        if not filename.endswith('.csv'):
            filename = filename + '.csv'

        trackers = ConvertionTracker.objects.all()
        model_fields = ConvertionTracker._meta.fields
        field_names = [field.name for field in model_fields]

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for row in trackers:
                values = []
                for field in field_names:
                    value = getattr(row, field)
                    if callable(value):
                        try:
                            value = value() or ''
                        except:
                            value = 'Error retrieving value'
                    if value is None:
                        value = ''
                    values.append(value)
                writer.writerow(values)





