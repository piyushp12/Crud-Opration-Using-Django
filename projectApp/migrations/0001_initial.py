# Generated by Django 4.0.6 on 2022-07-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=40)),
                ('last', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'crud',
            },
        ),
    ]