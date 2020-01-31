from apps.users.factories import UsersFactory
from apps.users.entities import UserEntity
from utils.db_utils import DBRepository


class UsersRepository(DBRepository):

    async def create_user(self, user_entity: UserEntity, password: str):
        sql = '''
            INSERT INTO users (email, name, password)
            VALUES ($1, $2, crypt($3, gen_salt('bf')))
        '''
        return await self._simple_execute(sql, user_entity.email, user_entity.name, password)

    async def get_user(self, email: str, password: str) -> UserEntity:
        sql = '''
            SELECT * FROM users
            WHERE email = $1 AND password = crypt($2, password)
        '''
        return await UsersFactory.from_record(await self._select_one(sql, email, password))

    async def get_user_by_id(self, user_id: int):
        sql = '''
            SELECT * FROM users
            WHERE user_id = $1
        '''
        return await UsersFactory.from_record(await self._select_one(sql, user_id))

    async def get_user_by_fields(self, user_id: int, name: str, email: str):
        sql = '''
            SELECT * FROM users
            WHERE user_id = $1 AND name = $2 AND email = $3
        '''
        return await UsersFactory.from_record(await self._select_one(sql, user_id, name, email))

    async def update_user_password(self, user_entity: UserEntity, new_pass: str):
        sql = '''
            UPDATE users SET password = crypt($1, gen_salt('bf'))
            WHERE user_id = $2
        '''
        return await self._simple_execute(sql, new_pass, user_entity.user_id)

    async def get_user_encrypted_password(self, user_id: int):
        sql = '''
            SELECT password from users
            WHERE user_id = $1
        '''
        password_record = await self._select_one(sql, user_id)
        return password_record['password']

    async def update_user(self, user_id: int, update_entity: UserEntity):
        sql = '''
            UPDATE users
            SET email = $1, name = $2
            WHERE user_id = $3
        '''
        return await self._simple_execute(sql, update_entity.email, update_entity.name, user_id)

    async def delete_user(self, user_id: int):
        sql = '''
            DELETE FROM users
            WHERE user_id = $1
        '''
        return await self._simple_execute(sql, user_id)
