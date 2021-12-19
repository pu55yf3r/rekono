from django_filters import rest_framework
from django_filters.rest_framework.filters import OrderingFilter
from resources.models import Wordlist


class WordlistFilter(rest_framework.FilterSet):
    o = OrderingFilter(fields=('name', 'type', 'creator'))

    class Meta:
        model = Wordlist
        fields = {
            'name': ['exact', 'contains', 'icontains'],
            'type': ['exact'],
            'creator': ['exact'],
            'creator__username': ['exact', 'iexact', 'contains', 'icontains'],
            'size': ['gte', 'lte', 'exact'],
        }
