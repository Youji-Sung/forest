from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile),
    path('<str:username>/delete/', views.user_delete),
]
