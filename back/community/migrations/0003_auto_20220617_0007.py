# Generated by Django 3.2.12 on 2022-06-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20220616_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='forest',
        ),
        migrations.RemoveField(
            model_name='article',
            name='using_date',
        ),
    ]
