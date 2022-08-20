from dataclasses import dataclass

from cms.services.structures import ComponentStructure


@dataclass
class HomeStructure(ComponentStructure):
    classes = []
    components = {}
