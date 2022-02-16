from django.urls import path
from . import views

urlpatterns =  [
    path ('', views.home, name = 'home'),
    path('businesses/', views.businesses_index, name='index'),
    path('businesses/<int:business_id>/', views.businesses_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('business/', views.business_index, name='index'),
    path('business/create/', views.BusinessCreate.as_view(), name='business_create'),
    path ('category', views.category, name = 'category')
]