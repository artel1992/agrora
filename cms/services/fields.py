import pickle
from dataclasses import dataclass, asdict

from django.db.models import Manager
from rest_framework.serializers import Field, JSONField

from cms.services.structures import ComponentStructure


class JSONDataClassField(Field):
    structure_class = ComponentStructure

    def to_internal_value(self, data):
        return self.structure_class(**data)

    def __init__(self, structure_class, *args, **kwargs):
        self.structure_class = structure_class
        super(JSONDataClassField, self).__init__(*args, **kwargs)


class RecursiveField(Field):
    def to_representation(self, value):
        serializer_class = self.parent.__class__
        if isinstance(value, Manager):
            return serializer_class(value.all(), many=True).data
        else:
            return serializer_class(value).data

    def to_internal_value(self, value):
        return [1, 2, 3]

    def __init__(self, many: bool = False, *args, **kwargs):
        self.many = many
        super(RecursiveField, self).__init__(*args, **kwargs)
