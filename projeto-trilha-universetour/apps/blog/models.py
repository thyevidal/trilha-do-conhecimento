from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    publicacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
