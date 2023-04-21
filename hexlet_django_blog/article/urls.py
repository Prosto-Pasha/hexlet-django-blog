from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import HomePageView
from hexlet_django_blog.article.views import IndexView
from hexlet_django_blog.article.views import ArticleFormCreateView
from hexlet_django_blog.article.views import ArticleFormEditView


# Маршрут 'articles_update' должен обязательно
# быть выше маршрута 'article_show', т.к.
# в противном случае будет выбираться первый
# подходящий по шаблону маршрут -  'article_show'

urlpatterns = [
    path('', IndexView.as_view(), name='articles',),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path(
        '<int:article_id>/',
        HomePageView.as_view(template_name='show.html'),
        name='article_show',
    ),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),

]