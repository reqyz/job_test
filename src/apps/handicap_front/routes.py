from apps.handicap_front.views import RegisterUserView, LoginUserView, UserPageView

routes = [
    ('GET', '/', RegisterUserView, 'f_create_user'),
    ('GET', '/login/', LoginUserView, 'f_login_user'),
    ('GET', '/user/', UserPageView, 'f_user_page'),
]
