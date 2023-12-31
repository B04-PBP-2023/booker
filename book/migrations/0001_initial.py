# Generated by Django 4.2.4 on 2023-10-28 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('stock', models.IntegerField(blank=True, default=10, null=True)),
                ('points_to_exchange', models.IntegerField(
                    blank=True, default=100, null=True)),
                ('for_sale', models.BooleanField(
                    blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoughtBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(
                    on_delete=django.db.models.deletion.RESTRICT, to='book.book')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('book', models.ForeignKey(
                    on_delete=django.db.models.deletion.RESTRICT, to='book.book')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
