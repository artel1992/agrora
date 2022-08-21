from rest_framework import serializers
from cms.models import Component, AppScript
from cms.services.fields import RecursiveField, JSONDataClassField
from cms.services.structures import ComponentStructure


class ComponentSerializer(serializers.ModelSerializer):
    structure = serializers.JSONField()
    children = RecursiveField(many=True, read_only=True)

    # title = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Component
        fields = ('id', 'name', 'title', 'structure', 'path', 'children', 'parent', 'sequence_number', 'level')
        extra_kwargs = {
            'parent': {'write_only': True, 'required': False},
            'title': {'required': False, 'allow_null': True, 'allow_blank': True},
        }


class AppScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppScript
        fields = ('id', 'name', 'path')
