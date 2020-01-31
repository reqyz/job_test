from apps.links.views import LinksViews, DownloadLinkView

routes = [
    ('GET', '/users/links/', LinksViews, 'get_links'),
    ('POST', '/users/links/', LinksViews, 'create_link'),
    ('PUT', '/users/links/{link_id}/', LinksViews, 'update_link'),
    ('DELETE', '/users/links/{link_id}/', LinksViews, 'delete_link'),

    ('GET', '/users/links/download/{link_id}/', DownloadLinkView, 'download_link'),
]
