# Generated by Django 5.1.1 on 2024-10-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0008_alter_negocio_rubro_alter_user_is_admin_negocio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='rubro',
            field=models.CharField(choices=[('tienda', 'Tienda'), ('restaurante', 'Restaurante'), ('tecnologia', 'Tecnología'), ('moda', 'Moda'), ('LocalesNocturnos', 'LocalesNocturnos')], max_length=20),
        ),
    ]
