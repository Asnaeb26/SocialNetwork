from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to='music/', null=False)

    def __repr__(self):
        return f'name - {self.name}'


class News(models.Model):
    image = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=255, blank=False, null=False)
    text = models.CharField(max_length=1000, blank=False, null=False)
