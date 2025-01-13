from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name='article_tags')

    def __str__(self):
        return self.title

    def get_tags(self):
        return ', '.join([str(i) for i in self.tag.all()])


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text
