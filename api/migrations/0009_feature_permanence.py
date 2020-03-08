# Generated by Django 3.0.3 on 2020-03-08 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0008_feature_categories")]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="permanence",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(10)],
            ),
        )
    ]
