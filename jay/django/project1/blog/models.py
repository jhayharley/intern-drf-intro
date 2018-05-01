from django.db import models

# Create your models here.
class Anime(models.Model):
    title          = models.CharField(max_length=120)
    description    = models.CharField(max_length=120)
    director       = models.CharField(max_length=120)
    release_date   = models.DateTimeField(auto_now_add=True)
    score          = models.CharField(max_length=120)
    picture        = models.ImageField(upload_to = 'static/media')

    def __str__(self):
        return '{}'.format(self.title)

class Breed(models.Model):
    name           = models.CharField(max_length=120)
    description    = models.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.name)

class Website(models.Model):
    name           = models.CharField(max_length=120)
    link           = models.URLField(max_length=120)
    owner          = models.CharField(max_length=120)
    logo           = models.ImageField(upload_to = 'static/media')
    def __str__(self):
        return '{}'.format(self.name)