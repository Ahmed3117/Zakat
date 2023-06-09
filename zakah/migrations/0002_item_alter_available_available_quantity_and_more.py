# Generated by Django 4.1.3 on 2023-05-10 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zakah', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='available',
            name='available_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='available',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakah.item'),
        ),
        migrations.AlterField(
            model_name='inbound',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakah.item'),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakah.item'),
        ),
    ]
