# Generated by Django 4.2.6 on 2023-10-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('trailer', models.URLField()),
                ('hero_name', models.CharField(blank=True, max_length=50, null=True)),
                ('heroine_name', models.CharField(blank=True, max_length=50, null=True)),
                ('director_name', models.CharField(blank=True, max_length=50, null=True)),
                ('producer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sideactor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('movie_poster', models.URLField()),
                ('heroimg', models.URLField()),
                ('heroineimg', models.URLField()),
                ('directorimg', models.URLField()),
                ('producerimg', models.URLField()),
                ('sideactorimg', models.URLField()),
                ('bgi', models.URLField()),
            ],
        ),
    ]
