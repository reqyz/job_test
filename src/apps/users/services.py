from apps.users.factories import UsersFactory
from apps.users.entities import UserEntity
from apps.users.presenters import UsersPresenter
from apps.users.repositories import UsersRepository
from utils.jwt_utils import jwt_encode, jwt_decode


class UsersService:

    def __init__(self, pool):
        self._pool = pool
        self.users_repo = UsersRepository(pool=pool)

    async def create_user(self, user_entity: UserEntity, password: str):
        return await self.users_repo.create_user(user_entity, password)

    async def get_user(self, email: str, password: str) -> UserEntity:
        return await self.users_repo.get_user(email, password)

    async def get_user_by_id(self, user_id: int):
        return await self.users_repo.get_user_by_id(user_id)

    async def update_user_password(self, user_entity: UserEntity, new_pass: str):
        return await self.users_repo.update_user_password(user_entity, new_pass)

    async def update_user(self, user_id: int, update_entity: UserEntity):
        return await self.users_repo.update_user(user_id, update_entity)

    async def delete_user(self, user_id: int):
        return await self.users_repo.delete_user(user_id)

    async def get_user_by_token(self, token: str):
        user_entity = await self.get_user_from_token(token)
        return await self.users_repo.get_user_by_fields(user_entity.user_id, user_entity.name, user_entity.email)

    async def get_user_token(self, user: UserEntity) -> str:
        secret = await self.users_repo.get_user_encrypted_password(user.user_id)
        return await jwt_encode(await UsersPresenter.to_dict(user), secret)

    async def get_user_from_token(self, token: str) -> UserEntity:
        user_dict = await jwt_decode(token, validate=False)
        secret = await self.users_repo.get_user_encrypted_password(user_dict['user_id'])
        return await UsersFactory.from_dict(await jwt_decode(token, secret))
