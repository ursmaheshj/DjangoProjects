# Generated by Django 5.0.2 on 2024-06-12 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4_examples', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pblish_in',
            new_name='publish_in',
        ),
    ]
