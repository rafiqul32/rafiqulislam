# Generated by Django 3.0.6 on 2020-05-18 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0002_auto_20200516_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='rent',
            field=models.FloatField(),
        ),
    ]
