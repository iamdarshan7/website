# Generated by Django 3.2.8 on 2021-11-10 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211110_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageinfo',
            name='article_image',
        ),
    ]
