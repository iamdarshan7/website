# Generated by Django 3.2.8 on 2021-10-09 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_announcement_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
