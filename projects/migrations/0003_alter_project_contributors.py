# Generated by Django 5.0.6 on 2024-06-27 14:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_created_type_project_created_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(blank=True, related_name='project_contributors', to=settings.AUTH_USER_MODEL),
        ),
    ]
