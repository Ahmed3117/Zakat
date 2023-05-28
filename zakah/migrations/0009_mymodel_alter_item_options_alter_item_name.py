# Generated by Django 4.1.3 on 2023-05-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zakah', '0008_alter_item_options_alter_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'عنصر', 'verbose_name_plural': 'عناصر'},
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
    ]
