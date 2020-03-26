from .category import Category
from .drawing_class import DrawingClass
from .view import View, ViewFeature

from .features.circle import Circle
from .features.feature import Feature, FeatureAttachment
from .features.line import Line
from .features.point import Point
from .features.polygon import MultiPolygon, Polygon

from .features.artificial_area import ArtificialArea
from .features.building import Building
from .features.parcel import Parcel
from .features.pathway import Pathway
from .features.wall import Wall

# Must be imported AFTER all features, so that they can be registered first
from .default_category import DefaultCategory
