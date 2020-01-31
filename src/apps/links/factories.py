from typing import Dict

from asyncpg.protocol.protocol import Record

from apps.links.entities import LinkEntity
from utils.factory_utils import BaseFactory


class LinksFactory(BaseFactory):
    @staticmethod
    async def from_record(record: Record) -> LinkEntity:
        return LinkEntity(
            link=record['link'],
            user_id=record['user_id'],
            link_id=record['link_id'],
        )

    @staticmethod
    async def from_dict(entity_dict: Dict) -> LinkEntity:
        return LinkEntity(
            link=entity_dict['link'],
            user_id=entity_dict.get('user_id'),
            link_id=entity_dict.get('link_id'),
        )
