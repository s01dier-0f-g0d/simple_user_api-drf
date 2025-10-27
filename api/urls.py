from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_home, name='api-home'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:user_id>/', views.user_detail, name='user-detail'),
    path('users/', views.search_users, name='search-users'),
]