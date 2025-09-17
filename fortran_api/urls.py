"""
Fortran API URLS
"""

from django.urls import path
from . import views

urlpatterns = [
    path('postResults/', views.get_fortran, name='post-fotran'),
    path('getResults/', views.create_fotran, name='create-fotran'),
]