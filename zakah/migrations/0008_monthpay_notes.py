# Generated by Django 4.1.3 on 2023-07-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zakah', '0007_monthpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthpay',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name=' ملاحظات'),
        ),
    ]
