from typing import List

import validators
from aiohttp import ClientSession

from apps.links.entities import LinkEntity
from apps.links.exceptions import StringIsNotAnUrl
from apps.links.repositories import LinksRepository


class LinksService:

    def __init__(self, pool):
        self._pool = pool
        self.link_repo = LinksRepository(pool=pool)

    async def create_link(self, user_id: int, link: str):
        if not validators.url(link):
            raise StringIsNotAnUrl
        return await self.link_repo.create_link(user_id, link)

    async def get_links(self, user_id: int) -> List[LinkEntity]:
        return await self.link_repo.get_links(user_id)

    async def update_link(self, link_id: int, update_entity: LinkEntity):
        return await self.link_repo.update_link(link_id, update_entity)

    async def delete_link(self, link_id: int):
        return await self.link_repo.delete_link(link_id)

    async def download_link(self, link_id: int, session: ClientSession):
        link_record = await self.link_repo.get_link(link_id)
        async with session.get(link_record.link, allow_redirects=True) as response:
            return await response.read(), response.content_type
