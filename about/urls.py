from .views import about_view
from django.urls import path

urlpatterns = [
    path('', about_view, name='about'),
]