from django.shortcuts import render
from core.models import Card, Employee, OperationLog, Responsible, Component
from django.shortcuts import get_object_or_404


def index(request):
    ctx = {'index': Card.objects.all()}
    return render(request, 'core/tables_dynamic.html', ctx)


def cards(request):
    ctx = {'cards': Card.objects.all()}
    return render(request, 'core/cards.html', ctx)


def card(request, pk):
    ctx = {'card': Card.objects.get(number=pk), 'components': Component.objects.filter(card_id=pk)}
    return render(request, 'core/card.html', ctx,)


def employees(request):
    ctx = {'employees': Employee.objects.all()}
    return render(request, 'core/employees.html', ctx)


def responsible(request):
    ctx = {'responsible': Responsible.objects.all()}
    return render(request, 'core/responsible.html', ctx)


def operations(request):
    ctx = {'operations': OperationLog.objects.all()}
    return render(request, 'core/operations.html', ctx)
