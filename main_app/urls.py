from django.urls import path
from . import views

urlpatterns =  [
    path ('', views.home, name = 'home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('business/', views.business_index, name='index'),
    path('business/create/', views.BusinessCreate.as_view(), name='business_create'),
]