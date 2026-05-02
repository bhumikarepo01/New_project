from django.urls import path
from . import views, api_views


urlpatterns = [

    path('', views.job_list, name='job_list'),
    path('create/', views.job_create, name='job_create'),
    path('detail/<int:pk>/', views.job_detail, name='job_detail'),

    path('api/companies/', api_views.company_list),
    path('api/companies/create/', api_views.company_create),
    path('api/companies/<int:pk>/', api_views.company_detail),
    path('api/companies/update/<int:pk>/', api_views.company_update),

]