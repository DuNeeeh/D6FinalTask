from django.db import models
from django.urls import reverse


class News(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все новости в категории будут доступны через поле news
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_each', args=[str(self.id)])


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name.title()


class Post(models.Model):
    NEWS = 'NW'
    ARTICLES = 'AR'
    CATEGORIES = [
        (NEWS, ('News')),
        (ARTICLES, ('Article')),
    ]

    categoryType = models.CharField(max_length=2, choices=CATEGORIES, default=ARTICLES)
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
