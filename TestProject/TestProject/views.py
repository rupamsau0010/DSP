# Written by me Rupam Sau.....

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    djText = request.GET.get('text', 'default')
    print(djText)
    return HttpResponse("<h1>Hello and welcome to Django</h1>")


def about(request):
    params = {'name': 'Rupam'}
    return render(request, 'index.html', params)
