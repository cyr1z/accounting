from django.shortcuts import render
from core.models import Card
from django.shortcuts import get_object_or_404


def index(request):
    ctx = {'product_list': Card.objects.all()}
    return render(request, 'core/index.html', ctx)