# Generated by Django 4.1 on 2022-08-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_employess'),
    ]

    operations = [
        migrations.AddField(
            model_name='employess',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='employess',
            name='domain',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='employess',
            name='number',
            field=models.IntegerField(default=None, unique=True),
        ),
    ]
