from rest_framework import filters, mixins, viewsets
from .permissions import IsAdminOrReadOnly

class ListCreateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    permission_class = [IsAdminOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter,]
    search_fields = ['=name']