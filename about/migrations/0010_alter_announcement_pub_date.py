# Generated by Django 3.2.7 on 2021-10-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_announcement_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
