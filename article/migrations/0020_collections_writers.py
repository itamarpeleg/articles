# Generated by Django 4.1 on 2022-09-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0019_collections_readers"),
    ]

    operations = [
        migrations.AddField(
            model_name="collections",
            name="writers",
            field=models.ManyToManyField(
                related_name="writers", to="article.user_article"
            ),
        ),
    ]
