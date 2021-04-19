# Generated by Django 3.2 on 2021-04-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('year_published', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Book Store',
                'verbose_name_plural': 'Book Stores',
            },
        ),
    ]
