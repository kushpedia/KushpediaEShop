
from . import views
from django.urls import path

urlpatterns = [
    path('', views.store,name = "store"),
    path('<slug:category_slug>/', views.store, name = "products_by_category"),
]
