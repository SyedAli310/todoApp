# Generated by Django 3.2.6 on 2021-08-19 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 19, 13, 16, 29, 347536, tzinfo=utc)),
        ),
    ]
