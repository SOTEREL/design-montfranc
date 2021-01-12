# Generated by Django 3.1.3 on 2021-01-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("designs", "0004_mapview_mapviewelement"),
    ]

    operations = [
        migrations.AddField(
            model_name="element",
            name="permanence",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (None, "Unspecified"),
                    (0, "Extremely simple to change"),
                    (1, "Simple to change"),
                    (2, "Moderately painful to change"),
                    (3, "Painful to change"),
                    (5, "Unchangeable"),
                ],
                null=True,
            ),
        ),
    ]
