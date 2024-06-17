from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    degree_title = models.CharField(
        max_length=150, verbose_name='Título Obtenido'
    )
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación'
    )
    update = models.DateTimeField(
        auto_now=True, verbose_name='Fecha Modificación'
    )

    # Pasos para convertir en español la aplación en el admin
    # y ordenación de los registros de acuerdo al campo 'created'
    # de forma descendente
    class Meta:
        verbose_name = 'Formación'
        verbose_name_plural = 'Formaciones'
        ordering = ['-created']

    # Con esta función logro mostrar en la lista de proyectos del admin
    # todos los proyectos con su titulo
    def __str__(self):
        return self.title


# Modelo para Skill
class Skills(models.Model):
    title = models.CharField(max_length=80, verbose_name='Título')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación'
    )
    update = models.DateTimeField(
        auto_now=True, verbose_name='Fecha Modificación'
    )

    # Pasos para convertir en español la aplación en el admin
    # y ordenación de los registros
    # de acuerdo al campo 'created' de forma descendente
    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['-created']

    # Con esta función logro mostrar en la lista de proyectos del admin,
    # todos los proyectos con su titulo
    def __str__(self):
        return self.title
