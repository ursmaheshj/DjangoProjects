# Generated by Django 5.0.2 on 2024-06-03 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1_inheritance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
    ]
