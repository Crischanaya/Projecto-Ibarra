# Generated by Django 3.1.2 on 2021-01-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SierraWeb', '0010_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='total_de_compra',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
