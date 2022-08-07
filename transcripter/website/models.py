# Create your models here.
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='cover/')
    video = models.FileField(max_length=100)
    file_path= models.CharField(max_length=100)

    def delete(self, *args, **kwargs):
        self.cover.delete()
        self.video.delete()
        super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title
