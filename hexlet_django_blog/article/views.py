from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy


# def index(request):  # (1)
#    # return HttpResponse('article')
#    return render(
#        request,
#        'index.html',
#        context={
#            'who': 'Hexlet',
#            'author': 'Internet'
#        }
#    )


class HomePageView(TemplateView):  # (2)

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Hexlet'
        context['author'] = 'Internet'
        return context

    def get(self, request, *args, **kwargs):
        tags=self.kwargs.get('tags', '---')
        article_id=self.kwargs.get('article_id', '---')
        if tags == '---' and article_id == '---':
            return redirect(reverse_lazy('article', kwargs={'tags': 'python', 'article_id': 42}))
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


# def index(request, tags='python', article_id='42'):
#    return redirect(f'/article/{tags}/{article_id}')