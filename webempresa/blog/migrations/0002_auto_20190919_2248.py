# Generated by Django 2.2.4 on 2019-09-19 20:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 19, 20, 48, 4, 931483, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
