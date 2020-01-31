from typing import Dict, List

from aiohttp import ClientSession

from apps.links.entities import LinkEntity
from apps.links.factories import LinksFactory
from apps.links.services import LinksService


class LinksController:

    def __init__(self, pool):
        self._pool = pool
        self.links_service = LinksService(pool)

    async def create_link(self, user_id: int, request_dict: Dict):
        link = request_dict['link']
        return await self.links_service.create_link(user_id, link)

    async def get_links(self, user_id: int) -> List[LinkEntity]:
        return await self.links_service.get_links(user_id)

    async def update_link(self, request_params: Dict, request_dict: Dict):
        link_id = request_params['link_id']
        link_entity = await LinksFactory.from_dict(request_dict)
        return await self.links_service.update_link(link_id, link_entity)

    async def delete_link(self, request_params: Dict):
        link_id = request_params['link_id']
        return await self.links_service.delete_link(link_id)

    async def download_link(self, request_params: Dict, session: ClientSession):
        link_id = request_params['link_id']
        return await self.links_service.download_link(link_id=link_id, session=session)
