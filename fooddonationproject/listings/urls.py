from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('create/', views.create_listing, name='create_listing'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
]
