# Generated by Django 3.2.8 on 2021-10-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20211030_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='email_link',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
