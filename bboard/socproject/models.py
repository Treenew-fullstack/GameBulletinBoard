from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class BulletinsCategory(models.Model):
    naming = models.CharField(max_length=32)

    def __str__(self):
        return self.naming


class Bulletins(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BulletinsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.pk}'


class Responses(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    respbulletins = models.ForeignKey(Bulletins, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text

