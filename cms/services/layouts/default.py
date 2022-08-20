from dataclasses import dataclass

from cms.services.structures import ComponentStructure


@dataclass
class DefaultStructure(ComponentStructure):
    classes = []
    components = {}
