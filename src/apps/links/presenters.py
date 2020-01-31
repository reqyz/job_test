from typing import Dict

from apps.links.entities import LinkEntity
from utils.presenter_utils import BasePresenter


class LinksPresenter(BasePresenter):

    @staticmethod
    async def to_dict(entity: LinkEntity) -> Dict:
        return {
            'link': entity.link,
            'user_id': entity.user_id,
            'link_id': entity.link_id,
        }

    @staticmethod
    async def to_api_response(entity: LinkEntity) -> Dict:
        return {
            'link_id': entity.link_id,
            'link': entity.link,
        }
