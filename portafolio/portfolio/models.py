from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    link = models.URLField(
        max_length=180, blank=True, null=True, verbose_name='Enlace'
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación'
    )
    update = models.DateTimeField(
        auto_now=True, verbose_name='Fecha Modificación'
    )

    # Pasos para convertir en español la aplicación en el admin
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    # Para que muestre el título como link para acceder desde el admin
    def __str__(self):
        return self.title
