# Generated by Django 3.2.8 on 2021-11-10 10:30

import app.validators
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='city_name')),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='consultancy_name')),
                ('logo_photo', models.ImageField(upload_to='covers/consultancy/')),
                ('desc', models.TextField(max_length=200)),
                ('special', models.BooleanField(default=False)),
                ('website_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'consultancies',
            },
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, null=True, validators=[app.validators.validate_number])),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='country_name')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='FeedBackByStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('feedback', models.TextField(max_length=100)),
                ('show_this', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='covers/feedback/')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='program_name')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='subject_name')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='university_name')),
                ('cover_photo', models.ImageField(upload_to='covers/uni_cover_photo/')),
                ('uni_logo', models.ImageField(upload_to='covers/uni_logo/')),
                ('desc', models.TextField(max_length=100, verbose_name='uni_short_description')),
                ('special', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'universities',
            },
        ),
        migrations.CreateModel(
            name='FilterForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fee', models.IntegerField(blank=True, null=True)),
                ('desc_1', ckeditor.fields.RichTextField(verbose_name='program_long_paragraph_description')),
                ('summer_intake_date', models.DateField(blank=True, null=True)),
                ('winter_intake_date', models.DateField(blank=True, null=True)),
                ('duration', models.FloatField()),
                ('requirement_1', models.CharField(max_length=200)),
                ('requirement_2', models.CharField(max_length=200)),
                ('requirement_3', models.CharField(max_length=200)),
                ('requirement_4', models.CharField(max_length=200)),
                ('requirement_5', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cities')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.countries')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.programstype')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.university')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, null=True, validators=[app.validators.validate_number])),
                ('files', models.FileField(upload_to='covers/application_file/')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.university')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.programstype')),
            ],
        ),
    ]
