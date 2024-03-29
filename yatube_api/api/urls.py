from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet, basename='post')
router_v1.register('v1/groups', GroupViewSet, basename='group')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(
    'v1/follow',
    FollowViewSet,
    basename='follow',
)

urlpatterns = [
    path('', include(router_v1.urls), ),
    path('v1/', include('djoser.urls.jwt')),
]
