from dataclasses import dataclass
from datetime import date

from utils.utils import gentle_convert


@dataclass
class UserEntity:
    name: str
    email: str
    user_id: int = None
    reg_date: date = None

    def __post_init__(self):
        self.user_id = gentle_convert(self.user_id, int)
