from dataclasses import dataclass, field
from typing import List, Dict

from cms.services.structures import ComponentStructure, Component, ComponentConfig, Levels


class DefaultLayoutConfig(ComponentConfig):
    pass


@dataclass
class DefaultStructure(ComponentStructure):
    classes: List[str] = field(default_factory=list)
    config: DefaultLayoutConfig = DefaultLayoutConfig()
    props = None
    level: str = Levels.page.value


@dataclass
class DefaultLayoutComponent(Component):
    name: str = 'default-layout'
    structure: DefaultStructure = DefaultStructure()
