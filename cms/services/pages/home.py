from dataclasses import dataclass, field
from typing import List, Dict

from cms.services.structures import ComponentStructure, Component, ComponentConfig, Levels


class HomeConfig(ComponentConfig):
    pass


@dataclass
class HomeStructure(ComponentStructure):
    classes: List[str] = field(default_factory=list)
    config: HomeConfig = HomeConfig()
    props = None
    level: str = Levels.root.value


@dataclass
class HomeComponent(Component):
    name: str = 'home-page'
    title: str = 'Главная страница'
    structure: HomeStructure = HomeStructure()
