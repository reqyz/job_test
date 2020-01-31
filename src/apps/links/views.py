import aiohttp
from aiohttp import web

from apps.links.controllers import LinksController
from apps.links.presenters import LinksPresenter
from utils.http_utils import BaseView, token_required, api_call


class LinksViews(BaseView):

    @token_required
    @api_call()
    async def get(self):
        data = await LinksController(self.pool).get_links(self.user.user_id)
        self.response = {
            'data': {'links': [await LinksPresenter.to_api_response(link) for link in data]},
            'status': 200,
        }

    @token_required
    @api_call(req_body=['link'])
    async def post(self):
        await LinksController(self.pool).create_link(self.user.user_id, self.request_data)

    @token_required
    @api_call(req_params=['link_id'], req_body=['link'])
    async def put(self):
        await LinksController(self.pool).update_link(self.match_info, self.request_data)

    @token_required
    @api_call(req_params=['link_id'])
    async def delete(self):
        await LinksController(self.pool).delete_link(self.match_info)


class DownloadLinkView(BaseView):

    @token_required
    async def get(self):
        async with aiohttp.ClientSession() as session:
            content, content_type = await LinksController(self.request.app.pool).download_link(self.request.match_info,
                                                                                               session)
        return web.Response(
            status=200,
            reason='OK',
            body=content,
            content_type=content_type
        )
