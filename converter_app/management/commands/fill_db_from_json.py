import json

from django.apps import apps
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


from converter_app.models import *


class Command(BaseCommand):
    help = "Create category"
#
#     def get(self, request, *args, **kwargs):
#         content_type_name = kwargs.get('name')
#
#         # Получаем content type по названию модели из url
#         content_type = get_object_or_404(ContentType, name=content_type_name)
#
#         # Получаем модель
#         model = content_type.get_for_model()
#         context = {
#             'objects': model.objects.all()
#         }
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='the name of file with data to fiil database')
    def handle(self, *args, **kwargs):
        filename = kwargs.get('filename')

        with open(filename) as json_file:
            data = json.load(json_file)

            for ele in data:
                category = [x for x in ele.keys()][0]
                app_models = apps.get_app_config('converter_app').get_models()
                category_class = [model for model in app_models if model.__name__ == category][0]
                try:
                    cols = [x for x in category_class._meta.get_fields()]
                    for i in range(len(ele[category][cols[1].name])):
                        new_item = category_class.objects.create()
                        for col in cols[1:]:
                            setattr(new_item, col.name, ele[category][col.name][i])
                        print(new_item)
                        new_item.save()

                except Exception as e:
                    print(f"Произошла ошибка: {e}")


