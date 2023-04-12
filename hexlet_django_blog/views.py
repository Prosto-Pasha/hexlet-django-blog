from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


# def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World',
#    })


def about(request):
    return render(request, 'about.html')