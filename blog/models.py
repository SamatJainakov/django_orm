from django.db import models


class AbstractUser(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)


class Author(AbstractUser):
    username = models.CharField(max_length=20)
    date_register = models.DateField()


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now=True)
