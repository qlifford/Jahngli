from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_product, name='show_products'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/<str:id>/', views.delete_product, name='delete_product'),
    path('update_product/<str:id>/', views.update_product, name='update_product'),
]
