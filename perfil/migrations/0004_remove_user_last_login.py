# Generated by Django 5.1.1 on 2024-10-17 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_alter_cliente_options_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
