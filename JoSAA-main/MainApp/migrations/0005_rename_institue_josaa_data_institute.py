# Generated by Django 4.2.2 on 2024-06-12 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_rename_institute_josaa_data_institue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='josaa_data',
            old_name='institue',
            new_name='institute',
        ),
    ]
