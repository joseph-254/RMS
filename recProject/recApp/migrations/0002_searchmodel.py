# Generated by Django 5.0.1 on 2024-01-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=255)),
            ],
        ),
    ]
