# Generated by Django 4.1 on 2022-08-31 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0017_collection_categories"),
    ]

    operations = [
        migrations.RenameModel(old_name="Collection", new_name="Collections",),
    ]
