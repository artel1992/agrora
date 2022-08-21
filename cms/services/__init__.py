from dataclasses import asdict
from typing import Optional

from cms.services.components.content import ContentComponent
from cms.services.components.slider import SliderStructure, SliderProps, SliderComponent
from cms.services.components.top_products import TopProductsComponent
from cms.services.layouts.default import DefaultLayoutComponent
from cms.services.pages.home import HomeComponent
from cms.services.structures import ComponentConfig


def get_empty_components(level: Optional[str]):
    return list(
        filter(lambda x: x.level == level if level is not None else True,
               [
                   asdict(SliderComponent()),
                   asdict(TopProductsComponent()),
                   asdict(ContentComponent()),
                   asdict(DefaultLayoutComponent()),
               ],
               )
    )


def get_empty_pages():
    return [
        asdict(HomeComponent())
    ]
