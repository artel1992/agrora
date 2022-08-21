from dataclasses import dataclass, field
from typing import List

from cms.services.structures import ComponentStructure, Component, ComponentConfig, Levels


@dataclass
class SliderConfig(ComponentConfig):
    has_children = False


@dataclass
class SliderProps:
    images: List[str] = field(default_factory=list)
    infinity: bool = True


@dataclass
class SliderStructure(ComponentStructure):
    props: SliderProps = SliderProps()
    config: ComponentConfig = SliderConfig()
    level: str   = Levels.layout.value


@dataclass
class SliderComponent(Component):
    name: str = 'slider-component'
    structure: SliderStructure = SliderStructure()
