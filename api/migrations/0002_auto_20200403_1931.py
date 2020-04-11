# Generated by Django 3.0.3 on 2020-04-03 17:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(name="feature", options={}),
        migrations.RemoveField(model_name="feature", name="polymorphic_ctype"),
        migrations.CreateModel(
            name="Parcel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "insee",
                    models.CharField(
                        max_length=5,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
                (
                    "section",
                    models.CharField(
                        max_length=2,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        max_length=4,
                        validators=[django.core.validators.MinLengthValidator(4)],
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Project"
                    ),
                ),
            ],
            options={"unique_together": {("project", "insee", "section", "number")}},
        ),
    ]