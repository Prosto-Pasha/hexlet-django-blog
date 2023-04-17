from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)  # Название статьи
    body = models.TextField()  # Тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}) {self.name}'