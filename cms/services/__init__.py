from typing import Dict

from django.db.models import Manager, Model


def create_tree(instance, serializer_class):
    if isinstance(instance, Manager):
        return serializer_class(instance.all(), many=True).data
        # tree = {}
        # for item in instance.iterator():
        #     tree[item.id] = serializer_class(item).data
        #     return tree
    else:
        return serializer_class(instance).data


def deconstruct_tree(value: Dict, model: Model):
    # result = []
    # for (ind, child) in value.items():
    #     result.append(model.objects.get(id=ind))
    return None
