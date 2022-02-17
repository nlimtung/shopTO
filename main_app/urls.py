from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns =  [
    path ('', views.home, name = 'home'),
    path('businesses/', views.businesses_index, name='index'),
    path('businesses/<int:business_id>/', views.businesses_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('businesses/create/', views.BusinessCreate.as_view(), name='businesses_create'),
    path ('category', views.category, name = 'category'),
    path('businesses/<int:pk>/update', views.BusinessesUpdate.as_view(), name='businesses_update'),
    path('businesses/<int:pk>/delete', views.BusinessesDelete.as_view(), name='businesses_delete'),
]