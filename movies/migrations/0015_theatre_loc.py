# Generated by Django 4.2.7 on 2023-11-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_remove_location_theatres_theatre_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='theatre',
            name='loc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
