# Generated by Django 5.0.6 on 2024-06-26 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='created_type',
            new_name='created_time',
        ),
    ]
