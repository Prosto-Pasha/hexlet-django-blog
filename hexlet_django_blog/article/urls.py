from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import HomePageView

urlpatterns = [
    # path('', views.index),  # (1)
    path('', HomePageView.as_view(template_name='index.html')),  # (2)
    path(
        '<str:tags>/<int:article_id>/',
        HomePageView.as_view(template_name='index.html'),
        name='article',
    ),
]