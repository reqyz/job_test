from apps.users.views import LoggedUsersView, UsersView

routes = [
    ('POST', '/users/login/', UsersView, 'user_login'),
    ('PUT', '/users/create/', UsersView, 'create_user'),

    ('GET', '/users/current/', LoggedUsersView, 'get_user_by_token'),
    ('POST', '/users/update/', LoggedUsersView, 'update_user'),
    ('PUT', '/users/update/pass/', LoggedUsersView, 'update_user_pass'),
    ('DELETE', '/users/', LoggedUsersView, 'delete_user'),
]
