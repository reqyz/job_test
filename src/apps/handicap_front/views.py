from aiohttp import web


class RegisterUserView(web.View):
    async def get(self):
        return web.FileResponse('apps/handicap_front/static/registration_page.html')


class LoginUserView(web.View):
    async def get(self):
        return web.FileResponse('apps/handicap_front/static/login_page.html')


class UserPageView(web.View):
    async def get(self):
        return web.FileResponse('apps/handicap_front/static/user_page.html')
