from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, get_token,
                    signup)

router_v1 = SimpleRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='rewiews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles')
router_v1.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router_v1.register(
    r'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', get_token),
    path('v1/auth/signup/', signup)
]
