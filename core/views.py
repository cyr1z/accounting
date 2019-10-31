from django.shortcuts import render
from core.models import Card, Employee
from django.shortcuts import get_object_or_404


def index(request):
    ctx = {'product_list': Card.objects.all()}
    return render(request, 'core/tables_dynamic.html', ctx)


def cards(request):
    ctx = {'cards': Card.objects.all()}
    return render(request, 'core/cards.html', ctx)

def employees(request):
    ctx = {'employees': Employee.objects.all()}
    return render(request, 'core/employees.html', ctx)