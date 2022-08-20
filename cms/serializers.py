from rest_framework import serializers
from cms.models import Component
from cms.services.fields import PickledField, RecursiveField
from cms.services.structures import ComponentStructure


class ComponentSerializer(serializers.ModelSerializer):
    structure = PickledField(structure_class=ComponentStructure)
    children = RecursiveField(required=False, many=True)

    class Meta:
        model = Component
        fields = ('id', 'name', 'structure', 'path', 'children', 'parent', 'sequence_number')
        extra_kwargs = {
            'children': {'read_only': True, 'required': False},
            'parent': {'write_only': True, 'required': False},
            'sequence_number': {'write_only': True, 'required': False},
        }
