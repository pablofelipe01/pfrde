from django.db import models

# Create your models here.


class Pferd(models.Model):
    name = models.CharField(max_length=300)
    line = models.CharField(max_length=300)
    breed = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    img_url = models.TextField()
    video_url = models.TextField()

    def __str__(self):
        return self.name
