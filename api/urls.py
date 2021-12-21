from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .views import TitleViewSet, GenreViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(router.urls),),
]
