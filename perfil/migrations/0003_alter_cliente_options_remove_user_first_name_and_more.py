# Generated by Django 5.1.1 on 2024-10-17 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_user_is_active_alter_user_is_admin_negocio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes del Marketplace'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]