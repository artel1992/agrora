from dataclasses import dataclass
from typing import List

from cms.services.structures import ComponentStructure


@dataclass
class SliderProps:
    images: List[str]
    infinity: bool = True


class SliderStructure(ComponentStructure):
    props: SliderProps
