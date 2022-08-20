import pickle
from dataclasses import dataclass, asdict

from django.db.models import Manager
from rest_framework.serializers import Field

from cms.services import create_tree, deconstruct_tree
from cms.services.structures import ComponentStructure


class PickledField(Field):
    structure_class = ComponentStructure

    def to_representation(self, value: ComponentStructure):
        if value:
            return asdict(value)
        return None

    def to_internal_value(self, data):
        return self.structure_class(**data)

    def __init__(self, structure_class, *args, **kwargs):
        self.structure_class = structure_class
        super(PickledField, self).__init__(*args, **kwargs)


class RecursiveField(Field):
    def to_representation(self, value):
        serializer_class = self.parent.__class__
        if isinstance(value, Manager):
            return serializer_class(value.all(), many=True).data
        else:
            return serializer_class(value).data

    def to_internal_value(self, value):
        return None

    def __init__(self, many: bool = False, *args, **kwargs):
        self.many = many
        kwargs.setdefault('read_only', True)
        super(RecursiveField, self).__init__(*args, **kwargs)
