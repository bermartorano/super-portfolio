# Generated by Django 4.2.3 on 2023-08-30 22:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="protfile",
            new_name="profile",
        ),
    ]
