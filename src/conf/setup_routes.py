import pkgutil
from importlib import import_module

import apps


def setup_routes(app):
    for importer, modname, ispkg in pkgutil.iter_modules(apps.__path__):
        routes = import_module(f'apps.{modname}.routes')
        register(app, routes.routes)


def register(app, routes: list):
    for method, path, handler, name in routes:
        app.router.add_route(method, path, handler, name=name)
