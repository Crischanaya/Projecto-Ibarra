# Generated by Django 3.1.2 on 2021-01-02 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SierraWeb', '0006_auto_20210101_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpaquete',
            name='nombre_paquete',
        ),
    ]
