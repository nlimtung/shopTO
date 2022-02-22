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
    path('businesses/<int:pk>/update', views.BusinessesUpdate.as_view(), name='businesses_update'),
    path('businesses/<int:pk>/delete', views.BusinessesDelete.as_view(), name='businesses_delete'),
    path('businesses/<int:business_id>/favourites/<user_id>', views.favourites_add, name = 'favourites_add'), 
    path('businesses/<int:business_id>/favourites_delete/<user_id>', views.favourites_delete, name = 'favourites_delete'), 

    path('businesses/favourites', views.favourite_list, name = 'favourite_list')
]