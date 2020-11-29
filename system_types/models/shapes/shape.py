from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from polymorphic.models import PolymorphicModel


class Shape(PolymorphicModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    map_projection = models.CharField(
        max_length=50, default=settings.LEAFLET_DEFAULT_PROJECTION
    )
    zoom = models.PositiveSmallIntegerField(default=settings.SATELLITE_LAYER_MAX_ZOOM)

    class Meta:
        unique_together = ("content_type", "object_id")

    def __init_subclass__(cls, *, style_cls, **kwargs):
        cls.style_cls = style_cls

    def __str__(self):
        return f"{self.__class__.__name__} of {self.content_object}"

    @property
    def is_drawable(self):
        raise NotImplementedError(
            f"{self.__class__.__name__}.is_drawable property must be implemented"
        )

    @property
    def centroid(self):
        raise NotImplementedError(
            f"{self.__class__.__name__}.centroid property must be implemented"
        )