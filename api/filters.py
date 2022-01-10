from django_filters.filters import CharFilter
from django_filters.rest_framework import FilterSet

from .models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(field_name='genre__slug')
    category = CharFilter(field_name='category__slug')
    name = CharFilter(lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('year',)
