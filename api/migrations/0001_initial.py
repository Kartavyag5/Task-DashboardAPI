# Generated by Django 3.2.5 on 2021-07-19 13:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Discription', models.TextField(max_length=400)),
                ('Phase', models.CharField(choices=[('To do', 'to do'), ('In Progress', 'in progress'), ('Review', 'review'), ('Done', 'done')], default='To do', max_length=20)),
                ('y_index', models.IntegerField(default=None, null=True)),
                ('Progress', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('start_time', models.DateTimeField()),
                ('Deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Tag', models.ManyToManyField(to='api.Tag')),
            ],
        ),
    ]
