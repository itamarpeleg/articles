# Generated by Django 4.1 on 2022-08-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0006_rename_category_categories_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="year_created",
            field=models.IntegerField(null=True),
        ),
    ]
