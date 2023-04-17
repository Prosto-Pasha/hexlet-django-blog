from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article


######
# 1
# admin.site.register(Article)
######


######
# 2
# class ArticleAdmin(admin.ModelAdmin):
#    search_fields = ['name', 'body']
#
# admin.site.register(Article, ArticleAdmin)
######


######
# 3
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#    search_fields = ['name', 'body']
######


######
# 4
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'timestamp') # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),) # Перечисляем поля для фильтрации
######
