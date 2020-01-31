from abc import ABCMeta
from typing import Dict

from asyncpg.protocol.protocol import Record


class BaseFactory(metaclass=ABCMeta):

    @staticmethod
    async def from_record(record: Record):
        raise NotImplementedError

    @staticmethod
    async def from_dict(entity_dict: Dict):
        raise NotImplementedError
