# Generated by Django 3.2.8 on 2021-10-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211030_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultancy',
            name='website_link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='website_link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
