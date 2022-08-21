from dataclasses import dataclass, field
from typing import List

from cms.services.structures import ComponentStructure, Component, ComponentConfig, Levels


@dataclass
class ContentConfig(ComponentConfig):
    has_children = False


@dataclass
class ContentProps:
    content: str = ''


@dataclass
class ContentStructure(ComponentStructure):
    props: ContentProps = ContentProps()
    config: ComponentConfig = ContentConfig()
    level: str = Levels.layout.value


@dataclass
class ContentComponent(Component):
    name: str = 'content-component'
    structure: ContentStructure = ContentStructure()
