# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('article')
    return render(
        request,
        'index.html',
        context={
            'who': 'Hexlet',
            'author': 'Internet'
        }
    )
