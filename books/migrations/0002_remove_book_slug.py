# Generated by Django 5.1.1 on 2024-10-15 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
