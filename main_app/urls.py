from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns =  [
    path ('', views.home, name = 'home'),
    path('businesses/', views.businesses_index, name='index'),
    path('businesses/<int:business_id>/', views.businesses_detail, name='detail'),
    path('myprofile/', views.my_profile, name='myprofile'),
    path('accounts/signup/', views.signup, name='signup'),
    path('businesses/create/', views.BusinessCreate.as_view(), name='businesses_create'),
    path ('category', views.category, name = 'category'),
    path('businesses/<int:pk>/update', views.BusinessesUpdate.as_view(), name='businesses_update'),
    path('businesses/<int:pk>/delete', views.BusinessesDelete.as_view(), name='businesses_delete'),
    path('business/<int:business_id>/add_product/', views.add_product, name='add_product'),
    path('business/<int:pk>/edit_product/', views.edit_product.as_view(), name='edit_product'),
    path('business/<int:pk>/delete_product/', views.delete_product.as_view(), name='delete_product'),
]