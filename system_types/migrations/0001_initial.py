# Generated by Django 3.1.3 on 2020-12-11 17:32

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import system_types.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ElementType",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(blank=True, default="")),
                ("needs", models.TextField(blank=True, default="")),
                ("contributions", models.TextField(blank=True, default="")),
            ],
            options={"verbose_name_plural": "element types", "ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="ElementTypeStyle",
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
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_system_types.elementtypestyle_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={"abstract": False, "base_manager_name": "objects",},
        ),
        migrations.CreateModel(
            name="Shape",
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
                ("object_id", models.PositiveIntegerField()),
                (
                    "map_projection",
                    models.CharField(default="EPSG:3857", max_length=50),
                ),
                ("edit_zoom", models.PositiveSmallIntegerField(default=19)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_system_types.shape_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={"unique_together": {("content_type", "object_id")},},
        ),
        migrations.CreateModel(
            name="Theme",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Circle",
            fields=[
                (
                    "shape_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.shape",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(blank=True, default=None, null=True),
                ),
                (
                    "radius",
                    models.FloatField(
                        default=1,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.shape",),
        ),
        migrations.CreateModel(
            name="CircleStyle",
            fields=[
                (
                    "elementtypestyle_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.elementtypestyle",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(default="#FFFFFF", max_length=18),
                ),
                ("weight", models.PositiveSmallIntegerField(default=2)),
                (
                    "opacity",
                    models.PositiveSmallIntegerField(
                        default=100,
                        validators=[django.core.validators.MaxValueValidator(100)],
                    ),
                ),
                (
                    "dash_array",
                    models.CharField(
                        blank=True,
                        help_text="Example: 5-5",
                        max_length=50,
                        validators=[system_types.models.validators.validate_dash_array],
                    ),
                ),
                ("icon", models.ImageField(null=True, upload_to="")),
            ],
            options={"abstract": False,},
            bases=("system_types.elementtypestyle", models.Model),
        ),
        migrations.CreateModel(
            name="Line",
            fields=[
                (
                    "shape_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.shape",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(blank=True, default=None, null=True),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.shape",),
        ),
        migrations.CreateModel(
            name="LineStyle",
            fields=[
                (
                    "elementtypestyle_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.elementtypestyle",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(default="#FFFFFF", max_length=18),
                ),
                ("weight", models.PositiveSmallIntegerField(default=2)),
                (
                    "opacity",
                    models.PositiveSmallIntegerField(
                        default=100,
                        validators=[django.core.validators.MaxValueValidator(100)],
                    ),
                ),
                (
                    "dash_array",
                    models.CharField(
                        blank=True,
                        help_text="Example: 5-5",
                        max_length=50,
                        validators=[system_types.models.validators.validate_dash_array],
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.elementtypestyle", models.Model),
        ),
        migrations.CreateModel(
            name="MultiPolygon",
            fields=[
                (
                    "shape_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.shape",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(blank=True, default=None, null=True),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.shape",),
        ),
        migrations.CreateModel(
            name="Point",
            fields=[
                (
                    "shape_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.shape",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(blank=True, default=None, null=True),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.shape",),
        ),
        migrations.CreateModel(
            name="PointStyle",
            fields=[
                (
                    "elementtypestyle_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.elementtypestyle",
                    ),
                ),
                ("icon", models.ImageField(null=True, upload_to="")),
            ],
            options={"abstract": False,},
            bases=("system_types.elementtypestyle", models.Model),
        ),
        migrations.CreateModel(
            name="Polygon",
            fields=[
                (
                    "shape_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.shape",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(blank=True, default=None, null=True),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.shape",),
        ),
        migrations.CreateModel(
            name="PolygonStyle",
            fields=[
                (
                    "elementtypestyle_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="system_types.elementtypestyle",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(default="#FFFFFF", max_length=18),
                ),
                ("weight", models.PositiveSmallIntegerField(default=2)),
                (
                    "opacity",
                    models.PositiveSmallIntegerField(
                        default=100,
                        validators=[django.core.validators.MaxValueValidator(100)],
                    ),
                ),
                (
                    "dash_array",
                    models.CharField(
                        blank=True,
                        help_text="Example: 5-5",
                        max_length=50,
                        validators=[system_types.models.validators.validate_dash_array],
                    ),
                ),
                (
                    "fill_color",
                    colorfield.fields.ColorField(default="#FFFFFF", max_length=18),
                ),
                (
                    "fill_opacity",
                    models.PositiveSmallIntegerField(
                        default=100,
                        validators=[django.core.validators.MaxValueValidator(100)],
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("system_types.elementtypestyle", models.Model),
        ),
        migrations.CreateModel(
            name="ThemedElementType",
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
                    "element_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="system_types.elementtype",
                    ),
                ),
                (
                    "shape_ctype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="contenttypes.contenttype",
                        validators=[
                            system_types.models.validators.validate_shape_ctype
                        ],
                    ),
                ),
                (
                    "theme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="system_types.theme",
                    ),
                ),
            ],
            options={
                "ordering": ["theme", "element_type"],
                "unique_together": {("theme", "element_type")},
            },
        ),
        migrations.AddField(
            model_name="theme",
            name="element_types",
            field=models.ManyToManyField(
                through="system_types.ThemedElementType", to="system_types.ElementType"
            ),
        ),
        migrations.AddField(
            model_name="elementtypestyle",
            name="themed_element_type",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="style",
                to="system_types.themedelementtype",
            ),
        ),
    ]
