from typing import List

from apps.links.entities import LinkEntity
from apps.links.factories import LinksFactory
from utils.db_utils import DBRepository


class LinksRepository(DBRepository):

    async def create_link(self, user_id: int, link: str):
        sql = '''
            INSERT INTO links (user_id, link)
            VALUES ($1, $2)
        '''
        return await self._simple_execute(sql, int(user_id), link)

    async def get_link(self, link_id: int) -> LinkEntity:
        sql = '''
            SELECT * FROM links
            WHERE link_id = $1
        '''
        return await LinksFactory.from_record(await self._select_one(sql, int(link_id)))

    async def get_links(self, user_id: int) -> List[LinkEntity]:
        sql = '''
            SELECT * FROM links
            WHERE user_id = $1
            ORDER BY link_id
        '''
        return [await LinksFactory.from_record(record) for record in
                await self._select_all(sql, int(user_id))]

    async def update_link(self, link_id: int, update_entity: LinkEntity):
        sql = '''
            UPDATE links
            SET link = $2
            WHERE link_id = $1
        '''
        return await self._simple_execute(sql, int(link_id), update_entity.link)

    async def delete_link(self, link_id: int):
        sql = '''
            DELETE FROM links
            WHERE link_id = $1
        '''
        return await self._simple_execute(sql, int(link_id))
