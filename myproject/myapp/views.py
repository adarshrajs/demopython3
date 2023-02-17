from django.http import HttpResponse
from django.shortcuts import render
from . models import destination, Team
# Create your views here.


def demo(request):
    a = destination.objects.all()
    c = Team.objects.all()
    return render(request, 'index.html', {'b': a, 'd': c})


