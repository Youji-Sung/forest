
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forests_list),
    path('<int:forest_id>/', views.forest_detail),
    path('<int:forest_id>/like', views.like_forest),
    path('<int:forest_id>/stamp', views.stamp_forest),
    path('<int:forest_id>/review/', views.review_create),
    path('<int:forest_id>/review/<int:review_pk>/', views.review_update_or_delete),
    path('<int:forest_id>/community/', views.community_create),   
    path('<int:forest_id>/community/<int:community_pk>/', views.community_update_or_delete), 
]