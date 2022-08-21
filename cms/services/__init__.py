from dataclasses import asdict
from typing import Optional

from cms.services.components.slider import SliderStructure, SliderProps, SliderComponent
from cms.services.layouts.default import DefaultLayoutComponent
from cms.services.structures import ComponentConfig


def get_empty_components_list(level: Optional[str]):
    return list(
        filter(lambda x: x.level == level if level is not None else True,
               [
                   asdict(SliderComponent()),
                   asdict(DefaultLayoutComponent()),
               ],
               )
    )
