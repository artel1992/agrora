from dataclasses import dataclass
from typing import Dict, Optional, Union, ForwardRef, List, Generic, TypeVar
from enum import Enum

ComponentStructureRef = ForwardRef('ComponentStructure')


class Levels(Enum):
    any = 'any'
    page = 'page'
    layout = 'layout'
    root = 'root'


@dataclass
class ComponentConfig:
    editable: bool = True
    has_children: bool = True
    deletable: bool = True


@dataclass
class ComponentStructure:
    config: ComponentConfig
    classes: Optional[Union[List[str], Dict[str, bool]]] = None
    props: Optional[Dict] = None
    level: str = Levels.any.value


@dataclass
class Component:
    name: str
    structure: ComponentStructure
    title: str = ''
    parent: Optional[int] = None
    path: Optional[str] = None
    sequence_number: int = 0
