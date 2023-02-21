from django.contrib import admin
from django.urls import path,include
from .views import movieview
urlpatterns = [
    path('',movieview.as_view())
]