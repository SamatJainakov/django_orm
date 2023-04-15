from blog.models import Author, Article, Publication


nursultan = Author.objects.create(name='Нурсултан Бердиев', email='nursultanberdiev@gmail.com',
                                  username='nursultanberdiev', date_register='2021-01-04')
veronika = Author.objects.create(name='Лю Вероника', email='ronilyu@gmail.com',
                                 username='ronik', date_register='2023-03-12')
chynara = Author.objects.create(name='Токтосунов Чынара', email='chynara0409@gmail.com',
                                username='chynara', date_register='2023-11-21')


article1 = Article.objects.create(title='Что нужно для разработки мобильных приложений: языки и тренды',
                                  author=nursultan)
article2 = Article.objects.create(title='Зачем нужно использовать кроссплатформенную систему', author=nursultan)
article3 = Article.objects.create(title='Сравниваем Java и Python или с чего лучше начать', author=nursultan)
article4 = Article.objects.create(title='Новый ChatGPT-4: в чем его особенность', author=veronika)
article5 = Article.objects.create(title='История компании Boston Dynamics. Как появлялись их роботы', author=chynara)


publication1 = Publication.objects.create(author=nursultan, article=article1)
publication2 = Publication.objects.create(author=nursultan, article=article2)
publication3 = Publication.objects.create(author=nursultan, article=article3)
publication4 = Publication.objects.create(author=veronika, article=article4)
publication5 = Publication.objects.create(author=chynara, article=article5)

authors = Author.objects.all()

date_reg_order = authors.order_by('date_register')
name_order = authors.filter(name__iexact='nursultan')
date_order_gt = authors.filter(date_register__gt='2022-10-10')


dict_pub = Publication.objects.values('author', 'article')
tuple_pub = Publication.objects.values_list('author', 'article')
contain_pub = authors.filter(name__contains='В')
