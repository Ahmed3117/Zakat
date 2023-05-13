# Generated by Django 4.1.3 on 2023-05-10 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zakah', '0002_item_alter_available_available_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbound',
            name='date',
            field=models.DateField(default=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='inbound',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='date',
            field=models.DateField(default=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
