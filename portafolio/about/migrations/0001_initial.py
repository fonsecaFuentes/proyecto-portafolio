# Generated by Django 5.0.6 on 2024-06-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('degree_title', models.CharField(max_length=150, verbose_name='Título Obtenido')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
            ],
            options={
                'verbose_name': 'Formación',
                'verbose_name_plural': 'Formaciones',
                'ordering': ['-created'],
            },
        ),
    ]
