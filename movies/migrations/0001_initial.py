# Generated by Django 5.1.4 on 2024-12-13 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kinolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(max_length=600, upload_to='kino/')),
                ('video_fayl', models.FileField(max_length=600, upload_to='')),
                ('genre', models.CharField(max_length=255)),
                ('sight_age', models.CharField(max_length=20)),
                ('reyting', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Multfilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(max_length=600, upload_to='multfilm/')),
                ('video_fayl', models.FileField(max_length=600, upload_to='multfilm/')),
                ('sight_age', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=255)),
                ('reyting', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(max_length=600, upload_to='serial/')),
                ('video_fayl', models.FileField(max_length=600, upload_to='serial/')),
                ('sight_age', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=255)),
                ('reyting', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Serial_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('part', models.IntegerField()),
                ('img', models.ImageField(max_length=600, upload_to='serial_item/')),
                ('video_fayl', models.FileField(max_length=600, upload_to='serial_item/')),
                ('reyting', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.serial')),
            ],
        ),
    ]
