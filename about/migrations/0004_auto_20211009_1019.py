# Generated by Django 3.2.8 on 2021-10-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_announcement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='announcement',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
