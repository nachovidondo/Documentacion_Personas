# Generated by Django 3.1.3 on 2021-03-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basemodel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now=True, verbose_name='fecha de creacion')),
                ('update_date', models.DateField(auto_now_add=True, verbose_name='fecha modificacion ')),
            ],
            options={
                'verbose_name': 'Modelo base',
            },
        ),
    ]
