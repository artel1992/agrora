from dataclasses import dataclass, field
from typing import List

from cms.services.structures import ComponentStructure, Component, ComponentConfig, Levels


@dataclass
class TopProductsConfig(ComponentConfig):
    has_children: bool = False


@dataclass
class ProductProps:
    title: str = ''
    subtitle: str = ''
    price: str = ''
    img: str = ''


@dataclass
class TopProductsProps:
    products: List[ProductProps] = field(default_factory=list)


@dataclass
class TopProductsStructure(ComponentStructure):
    props: TopProductsProps = TopProductsProps()
    config: ComponentConfig = TopProductsConfig()
    level: str = Levels.layout.value


@dataclass
class TopProductsComponent(Component):
    name: str = 'top-products'
    structure: TopProductsStructure = TopProductsStructure()
