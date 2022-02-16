
from .models import Business

import django_filters


class BusinessFilter(django_filters.FilterSet):

    class Meta:
        model = Business
        fields = ['category']
    
