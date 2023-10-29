from django.db import migrations, models
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books.json")


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('reviews', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('genre', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RunPython(load_my_initial_data),
    ]