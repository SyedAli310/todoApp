# Generated by Django 3.2.6 on 2021-08-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '1️'), ('2', '2️'), ('3', '3️'), ('4', '4️'), ('5', '5️')], max_length=5),
        ),
    ]
