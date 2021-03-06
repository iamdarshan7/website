# Generated by Django 3.2.8 on 2021-11-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20211110_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageinfo',
            name='article_image',
            field=models.ImageField(default=2020, upload_to='covers/homepage/', verbose_name='Article_background_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepageinfo',
            name='stats_image',
            field=models.ImageField(default=2020, upload_to='covers/homepage/', verbose_name='Stats_background_image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='button_name2',
            field=models.CharField(max_length=100, verbose_name='talk_to_us_button'),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='heading_first_image',
            field=models.ImageField(upload_to='covers/homepage/', verbose_name='HomePage_background_image1'),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='heading_second_image',
            field=models.ImageField(upload_to='covers/homepage/', verbose_name='HomePage_background_image2'),
        ),
    ]
