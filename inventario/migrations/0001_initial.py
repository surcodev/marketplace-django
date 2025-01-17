# Generated by Django 5.1.1 on 2024-11-06 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rubro', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='inventario.rubro')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_subcategoria', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='inventario.categoria')),
            ],
        ),
    ]
