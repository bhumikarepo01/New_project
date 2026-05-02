from django.urls import path
from . import views, api_views

urlpatterns = [

    # Django Views
    path('', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),

    # DRF API
    path('api/books/', api_views.book_list_create),
    path('api/books/<int:pk>/', api_views.book_detail_update),
    path('book/create/', views.book_create, name='book_create'),
]