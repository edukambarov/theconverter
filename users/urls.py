from django.urls import path, include
from .views import Register
from converter_app.views import index

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('register/', Register.as_view(), name='register'),
]