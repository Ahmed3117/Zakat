# Generated by Django 4.1.3 on 2023-05-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zakah', '0013_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inoutcommon',
            name='category',
        ),
    ]
