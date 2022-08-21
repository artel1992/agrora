from rest_framework import serializers
from cms.models import Component
from cms.services.fields import RecursiveField, JSONDataClassField
from cms.services.structures import ComponentStructure


class ComponentSerializer(serializers.ModelSerializer):
    structure = serializers.JSONField()
    children = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Component
        fields = ('id', 'name', 'structure', 'path', 'children', 'parent', 'sequence_number', 'level')
        extra_kwargs = {
            'parent': {'write_only': True, 'required': False},
        }
