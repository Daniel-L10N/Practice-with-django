# Generated by Django 5.0 on 2024-02-19 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='preority',
            new_name='priority',
        ),
    ]
