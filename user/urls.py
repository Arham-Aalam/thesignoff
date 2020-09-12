from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_root),
    path('submittshirt/<int:tid>/<str:name>/', views.register_user),
]