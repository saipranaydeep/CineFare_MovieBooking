# Generated by Django 4.2.6 on 2023-10-31 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_moviecomment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecomment',
            name='parent',
        ),
    ]
