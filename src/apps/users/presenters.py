from typing import Dict

from apps.users.entities import UserEntity
from utils.presenter_utils import BasePresenter


class UsersPresenter(BasePresenter):

    @staticmethod
    async def to_dict(entity: UserEntity) -> Dict:
        return {
            'user_id': entity.user_id,
            'email': entity.email,
            'name': entity.name,
        }
