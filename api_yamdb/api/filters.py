import django_filters.rest_framework as django_filters
from django_filters.rest_framework import FilterSet
from reviews.models import Title


class FilterForTitle(FilterSet):
    genre = django_filters.CharFilter(field_name='genre__slug')
    category = django_filters.CharFilter(field_name='category__slug')
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('year',)
