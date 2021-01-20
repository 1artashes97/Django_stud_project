from django.db import models
import datetime

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('article name', max_length=200) #VarChar tipna 200-250 simvol
    article_text = models.TextField('article text')
    article_date = models.DateTimeField('publish data')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.article_date >= (timezone.now() - datetime.timedelta(days = 7)) #veradardznum e true, ete art.date 7 oric meca

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    author_name = models.CharField('author name', max_length=200)
    comment_text = models.CharField('comment text', max_length=200)

    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'