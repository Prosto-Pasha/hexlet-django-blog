from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Название статьи'
        }
    ))
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Тело статьи'
        }
    ))

    class Meta:
        model = Article
        fields = ['name', 'body']