# Generated by Django 5.1.1 on 2024-10-11 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0014_alter_administrador_departamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='nombre_discoteca',
            new_name='nombre_negocio',
        ),
    ]