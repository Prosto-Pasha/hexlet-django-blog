# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Hexlet'
        context['author'] = 'Internet'
        return context


# def index(request):
#    # return HttpResponse('article')
#    return render(
#        request,
#        'index.html',
#        context={
#            'who': 'Hexlet',
#            'author': 'Internet'
#        }
#    )
