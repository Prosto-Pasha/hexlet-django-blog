from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


# def index(request, tags='python', article_id='42'):
#    return redirect(f'/article/{tags}/{article_id}')


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


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()  # [:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)

        # Если добавлять сообщение здесь, то оно дублируется при редирректе на 'article'

        if form.is_valid(): # Если данные корректные, то сохраняем данные формы

            # Add message
            # messages.add_message(request, messages.INFO, 'Статья успешно добавлена')
            messages.info(request, 'Статья успешно добавлена')

            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class HomePageView(TemplateView):  # (2)

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Hexlet'
        context['author'] = 'Internet'
        return context

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })
        # tags = self.kwargs.get('tags', '---')
        # article_id = self.kwargs.get('article_id', '---')
        # if tags == '---' and article_id == '---':
        #    return redirect(reverse_lazy('article', kwargs={'tags': 'python', 'article_id': 42}))
        # return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.info(request, 'Статья успешно обновлена')
            return redirect('articles')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDestroyView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            messages.info(request, 'Статья успешно удалена')
            article.delete()
        else:
            messages.info(request, 'Ошибка удаления статьи')
        return redirect('articles')