# Generated by Django 5.1.4 on 2024-12-13 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(max_length=600, upload_to='anime/')),
                ('video_fayl', models.FileField(max_length=600, upload_to='anime/')),
                ('genre', models.CharField(max_length=255)),
                ('sight_age', models.CharField(max_length=20)),
                ('reyting', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Anime_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('part', models.IntegerField()),
                ('img', models.ImageField(max_length=600, upload_to='anime_item/')),
                ('video_fayl', models.FileField(max_length=600, upload_to='anime_item/')),
                ('reyting', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.anime')),
            ],
        ),
    ]
