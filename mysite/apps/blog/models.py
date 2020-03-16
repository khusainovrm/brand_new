from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=200)
    text = models.TextField("Text")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    me = User.objects.get (username='rinat')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-published_date',)
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField("Text")
    created = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created",)



class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Поиск"
        verbose_name_plural = "Поиск"
        ordering = ("-created",)

    def __str__(self):
        return self.search