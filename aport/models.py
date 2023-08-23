from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='portfolio/')
