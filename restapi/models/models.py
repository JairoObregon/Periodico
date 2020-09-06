from django.db import models

# Create your models here.
class category (models.Model):
    nombreCategoria = models.CharField(max_length=100,verbose_name='nombreCategoria')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
            verbose_name = "categoria"
            verbose_name_plural = "categorias"
            ordering = ['-created',]

    def __str__(self):
        return self.nombreCategoria

class post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    description = models.TextField(verbose_name="Descripcion")
    category = models.ForeignKey(category,on_delete=models.CASCADE, verbose_name="categoria")
    imagen = models.ImageField(upload_to='imagenes')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name='post'
        verbose_name_plural='post'
        ordering = ['-created',]

    def __str__(self):
        return self.title


class imagenes (models.Model):
    autor = models.CharField(max_length=100,verbose_name='nombre')
    imagen = models.ImageField(upload_to='imagenesPotada')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
            verbose_name = "autor"
            verbose_name_plural = "autores"
            ordering = ['-created',]

    def __str__(self):
        return self.autor