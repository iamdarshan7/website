# Generated by Django 3.2.8 on 2021-11-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_filterform_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterform',
            name='fee',
            field=models.CharField(default='N/A', max_length=10),
        ),
    ]
