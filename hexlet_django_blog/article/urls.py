from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import HomePageView
from hexlet_django_blog.article.views import IndexView
from hexlet_django_blog.article.views import ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='articles',),
    # path(
    #    '<str:tags>/<int:article_id>/',
    #    HomePageView.as_view(template_name='index.html'),
    #    name='article',
    # ),
    path(
        '<int:article_id>/',
        HomePageView.as_view(template_name='show.html'),
        name='article_show',
    ),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),

]