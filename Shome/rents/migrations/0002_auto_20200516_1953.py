# Generated by Django 3.0.6 on 2020-05-16 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rents.Flat'),
        ),
    ]
