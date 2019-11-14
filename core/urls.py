from . views import cards, index, card, responsible, employees, operations, employee, responsible_profile
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('cards/', cards, name='cards'),
    path('cards/<pk>/', card, name='card'),
    path('responsible/', responsible, name='responsible'),
    path('employees/', employees, name='employees'),
    path('employees/<pk>/', employee, name='employee'),
    path('responsible_profile/<pk>/', responsible_profile, name='responsible_profile'),
    path('operations/', operations, name='operations'),
]