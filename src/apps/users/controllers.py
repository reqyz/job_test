from typing import Dict

from apps.users.factories import UsersFactory
from apps.users.services import UsersService
from utils.exeptions import NotFoundException


class UsersController:

    def __init__(self, pool):
        self._pool = pool
        self.users_service = UsersService(pool)

    async def get_user_by_token(self, token: str):
        return await self.users_service.get_user_by_token(token)

    async def login_user(self, request_dict: Dict) -> str:
        email = request_dict['email']
        password = request_dict['password']
        user_entity = await self.users_service.get_user(email, password)
        return await self.users_service.get_user_token(user_entity)

    async def create_user(self, request_dict: Dict) -> str:
        password = request_dict['password']
        new_user_entity = await UsersFactory.from_dict(request_dict)
        try:
            user_entity = await self.users_service.get_user(new_user_entity.email, password)
        except NotFoundException:
            user_entity = None
        if not user_entity:
            await self.users_service.create_user(new_user_entity, password)
        registered_user = user_entity if user_entity else await self.users_service.get_user(new_user_entity.email,
                                                                                            password)
        return await self.users_service.get_user_token(registered_user)

    async def update_user(self, request_dict: Dict, user_token: str) -> str:
        old_user = await self.users_service.get_user_from_token(user_token)
        update_to = await UsersFactory.from_dict(request_dict)
        await self.users_service.update_user(old_user.user_id, update_to)
        updated_user = await self.users_service.get_user_by_id(old_user.user_id)
        return await self.users_service.get_user_token(updated_user)

    async def update_password(self, user_token: str, request_dict: Dict) -> str:
        new_password = request_dict['new_password']
        user_entity = await self.users_service.get_user_from_token(user_token)
        await self.users_service.update_user_password(user_entity, new_password)
        return await self.users_service.get_user_token(user_entity)

    async def delete_user(self, user_token: str) -> bool:
        user_entity = await self.users_service.get_user_from_token(user_token)
        await self.users_service.get_user_by_id(user_entity.user_id)
        await self.users_service.delete_user(user_entity.user_id)
        return True
