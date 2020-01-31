from dataclasses import dataclass, field
from typing import List, Dict

from utils.exeptions import NotEnoughData


@dataclass
class SimpleValidator:
    required_fields: List[str] = field(default_factory=list)
    validating_dict: Dict = field(default_factory=dict)

    def __post_init__(self):
        missing_fields = [fld for fld in self.required_fields if fld not in self.validating_dict.keys()]
        if missing_fields:
            raise NotEnoughData(message=f'missing fields: {", ".join(missing_fields)}')
