from json import JSONDecodeError
from typing import List

import ujson
from aiohttp import web
from aiohttp.web_response import json_response
from jwt import InvalidSignatureError

from apps.users.entities import UserEntity
from apps.users.services import UsersService
from utils.exeptions import BaseApiException, NotFoundException
from utils.validation import SimpleValidator


class BaseView(web.View):
    pool = None
    request_data = None
    match_info = None
    token = None
    response = None
    user: UserEntity = None

    def __call__(self, *args, **kwargs):
        return self.response if self.response else {'data': {'result': 'ok'}, 'status': 200}


async def setup_view(view: web.View):
    request = view.request
    view.pool = request.app.pool
    view.request_data = {}
    view.match_info = request.match_info
    try:
        view.request_data = await request.json()
    except JSONDecodeError:
        pass


async def return_json(**kwargs):
    return json_response(**kwargs, dumps=ujson.dumps)


def token_required(func):
    async def _decorator(self, *args, **kwargs):
        try:
            token = self.request.headers['token']
            user = await UsersService(self.request.app.pool).get_user_by_token(token)
        except (KeyError, NotFoundException, InvalidSignatureError):
            return await return_json(data={'error': 'access denied'}, status=403)
        self.token = token
        self.user = user
        return await func(self, *args, **kwargs)

    return _decorator


def api_call(*, req_params: List[str] = None, req_body: List[str] = None):
    def _api_call(func):
        async def _decorator(self, *args, **kwargs):
            try:
                await setup_view(self)
                if req_body:
                    SimpleValidator(req_body, self.request_data)
                if req_params:
                    SimpleValidator(req_params, self.match_info)
                await func(self, *args, **kwargs)
                result = self()
                if self.token:
                    result['headers'] = {'token': self.token}
                return await return_json(**result)
            except BaseApiException as e:
                return await return_json(data={'error': e.message}, status=e.status)

        return _decorator

    return _api_call
