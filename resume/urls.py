from django.contrib import admin
from django.urls import path, include
from resume import views

urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name="result")
]