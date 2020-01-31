from typing import Dict

from asyncpg.protocol.protocol import Record

from apps.users.entities import UserEntity
from utils.factory_utils import BaseFactory


class UsersFactory(BaseFactory):

    @staticmethod
    async def from_dict(entity_dict: Dict) -> UserEntity:
        return UserEntity(
            user_id=entity_dict.get('user_id', None),
            name=entity_dict['name'],
            email=entity_dict['email'],
            reg_date=entity_dict.get('reg_date', None),
        )

    @staticmethod
    async def from_record(record: Record) -> UserEntity:
        return UserEntity(
            user_id=record['user_id'],
            name=record['name'],
            email=record['email'],
            reg_date=record.get('reg_date', None),
        )
