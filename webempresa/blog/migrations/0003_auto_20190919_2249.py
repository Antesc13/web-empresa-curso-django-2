# Generated by Django 2.2.4 on 2019-09-19 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190919_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]