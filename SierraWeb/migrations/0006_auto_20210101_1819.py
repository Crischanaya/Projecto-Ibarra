# Generated by Django 3.1.2 on 2021-01-02 01:19

import SierraWeb.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SierraWeb', '0005_userpaquete_nombre_paquete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpaquete',
            name='nombre_paquete',
            field=models.TextField(db_column='nombre', verbose_name=SierraWeb.models.Paquetes),
        ),
    ]
