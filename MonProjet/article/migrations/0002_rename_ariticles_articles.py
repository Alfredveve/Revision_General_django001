# Generated by Django 5.0.6 on 2024-06-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Ariticles",
            new_name="Articles",
        ),
    ]
