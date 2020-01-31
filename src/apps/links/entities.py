from dataclasses import dataclass

from utils.utils import gentle_convert


@dataclass
class LinkEntity:
    link: str
    user_id: int
    link_id: int = None

    def __post_init__(self):
        self.user_id = gentle_convert(self.user_id, int)
        self.link_id = gentle_convert(self.link_id, int)
