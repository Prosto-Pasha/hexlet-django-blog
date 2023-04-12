from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(template_name='index.html')),
    # path('', views.index),
]