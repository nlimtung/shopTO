from django.db import models
from datetime import date
from django.contrib.auth.models import User


CATEGORY = (
    ('Other', 'Other'),
    ('Home', 'Home'),
    ('Books', 'Books'),
    ('Food', 'Food'),
    ('Music', 'Music'),
    ('Jewelry', 'Jewelry'),
    ('Pets', 'Pets'),
    ('Stationery', 'Stationery'),
    ('Clothes', 'Clothes')
)

class Business(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 100)
    website = models.URLField(max_length = 200)
    description = models.CharField(max_length=1000)
    category = models.CharField(
        max_length=10,
        choices=CATEGORY,
        default=CATEGORY[0][0]
    )
    image = models.ImageField(upload_to='businesscollector/',default='default.png',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField(
        User, related_name = 'favourite', default=None, blank=True)
    def __str__(self):
        return self.name

