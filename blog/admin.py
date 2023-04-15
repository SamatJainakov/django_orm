from django.contrib import admin
from .models import Publication, Article, Author


admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Article)
