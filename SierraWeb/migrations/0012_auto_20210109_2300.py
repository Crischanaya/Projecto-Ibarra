# Generated by Django 3.1.2 on 2021-01-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SierraWeb', '0011_compra_total_de_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='id_compra',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
