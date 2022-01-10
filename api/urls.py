from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews'),
router.register(r'titles/(?P<title_id>\d+)/reviews/'
                r'(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls),),
]
