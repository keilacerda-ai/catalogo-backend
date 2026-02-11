from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, related_name='libros', on_delete=models.CASCADE)
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.titulo
