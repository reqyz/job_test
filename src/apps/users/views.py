from apps.users.controllers import UsersController
from utils.http_utils import api_call, BaseView, token_required


class LoggedUsersView(BaseView):

    @token_required
    @api_call()
    async def get(self):
        self.response = {'data': {'user': await UsersController(self.pool).get_user_by_token(self.token)}}

    @token_required
    @api_call()
    async def post(self):
        self.token = await UsersController(self.pool).update_user(self.request_data, self.token)

    @token_required
    @api_call(req_body=['new_password'])
    async def put(self):
        self.token = await UsersController(self.pool).update_password(self.token, self.request_data)

    @token_required
    @api_call()
    async def delete(self):
        await UsersController(self.pool).delete_user(self.token)
        self.token = None


class UsersView(BaseView):

    @api_call(req_body=['password', 'name', 'email'])
    async def put(self):
        self.token = await UsersController(self.pool).create_user(self.request_data)

    @api_call(req_body=['email', 'password'])
    async def post(self):
        self.token = await UsersController(self.pool).login_user(self.request_data)
