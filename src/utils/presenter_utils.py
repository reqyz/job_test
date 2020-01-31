from abc import ABCMeta
from typing import Dict


class BasePresenter(metaclass=ABCMeta):

    @staticmethod
    async def to_dict(entity) -> Dict:
        raise NotImplementedError
