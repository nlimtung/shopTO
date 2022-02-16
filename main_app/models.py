from django.db import models
from datetime import date
from django.contrib.auth.models import User
import django_filters


CATEGORY = (
    ('Other', 'Other'),
    ('Home', 'Home'),
    ('Books', 'Books'),
    ('Clothes', 'Clothes')
)

class Business(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 100)
    website = models.URLField(max_length = 200)
    category = models.CharField(
        max_length=10,
        choices=CATEGORY,
        default=CATEGORY[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BusinessFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Business
        fields = ['category']