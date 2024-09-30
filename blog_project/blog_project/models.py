from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
