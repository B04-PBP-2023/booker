# Generated by Django 4.2.4 on 2023-10-28 15:07

from django.db import migrations
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books.json")


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
