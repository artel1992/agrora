from dataclasses import dataclass
from typing import Dict, Optional, Union, ForwardRef, List, Generic, TypeVar

ComponentStructureRef = ForwardRef('ComponentStructure')


@dataclass
class ComponentStructure:
    classes: Optional[Union[List[str], Dict[str, bool]]] = None
    props: Optional[Dict] = None
