# Generated by Django 5.0.1 on 2024-01-25 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recApp', '0004_remove_filesmodel_file_filesmodel_file_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recmodel',
            name='file_to',
        ),
        migrations.DeleteModel(
            name='FilesModel',
        ),
    ]
