# Generated by Django 3.0.3 on 2020-03-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("api", "0014_auto_20200319_1727")]

    operations = [
        migrations.CreateModel(
            name="ViewTileLayer",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("geoportal.satellite", "geoportal.satellite"),
                            ("geoportal.cadastre", "geoportal.cadastre"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tile_layers",
                        to="api.View",
                    ),
                ),
            ],
            options={"unique_together": {("view", "name")}},
        )
    ]
