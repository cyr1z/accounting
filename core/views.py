from django.shortcuts import render
from core.models import Card, Employee, OperationLog, Responsible, Component, Account, SubAccount
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


def index(request):
    ctx = {'index': Card.objects.all()}
    return render(request, 'core/tables_dynamic.html', ctx)


def cards(request):
    cards_filtered = Card.objects.all()
    ctx = {}
    if request.method == 'POST':
        cf = request.POST
        ctx_cf = {}
        if 'acc' in cf and cf['acc']:
            i = int(cf['acc'])
            if i:
                cards_filtered = cards_filtered.filter(account=i)
                ctx_cf['acc'] = i
        if 'subacc' in cf and cf['subacc']:
            i = int(cf['subacc'])
            if i:
                cards_filtered = cards_filtered.filter(sub_account=i)
                ctx_cf['subacc'] = i
        if 'resp' in cf and cf['resp']:
            i = int(cf['resp'])
            if i:
                cards_filtered = cards_filtered.filter(financially_responsible__pk=i)
                ctx_cf['resp'] = i
        if ctx_cf:
            ctx['cf'] = ctx_cf

    ctx['cards'] = cards_filtered
    ctx['accounts'] = Account.objects.all()
    ctx['subaccounts'] = SubAccount.objects.all()
    ctx['responsibles'] = Responsible.objects.all()

    return render(request, 'core/cards.html', ctx)


def card(request, pk):
    ctx = {'card': Card.objects.get(number=pk), 'components': Component.objects.filter(card_id=pk)}
    return render(request, 'core/card.html', ctx,)


def employees(request):
    ctx = {'employees': Employee.objects.all()}
    return render(request, 'core/employees.html', ctx)


def employee(request, pk):
    ctx = {'employee': Employee.objects.get(pk=pk)}
    return render(request, 'core/profile.html', ctx,)


def responsible_profile(request, pk):
    ctx = {'responsible_profile': Responsible.objects.get(pk=pk)}
    return render(request, 'core/responsible_profile.html', ctx,)


def responsible(request):
    ctx = {'responsible': Responsible.objects.all()}
    return render(request, 'core/responsible.html', ctx)


def operations(request):
    ctx = {'operations': OperationLog.objects.all()}
    return render(request, 'core/operations.html', ctx)
