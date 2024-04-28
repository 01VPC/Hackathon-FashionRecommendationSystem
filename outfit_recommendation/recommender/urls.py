from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_outfit, name='recommend_outfit'),
    path('recommend/', views.recommend_items, name='recommend_items'),
]
