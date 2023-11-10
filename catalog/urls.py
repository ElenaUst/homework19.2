from django.urls import path

from catalog.views import index, contact

urlpatterns = [
    path('', index, name='Главная'),
    path('contacts/', contact, name='Контакты')
]