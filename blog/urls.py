from django.urls import path, include
from blog import views

product_patterns = [
    path("", views.products),
    path("new/", views.new),
    path("top/", views.top),
]

urlpatterns = [
    path("", views.index),
    path("products/", include(product_patterns)),
]