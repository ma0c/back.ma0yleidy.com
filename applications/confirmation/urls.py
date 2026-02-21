from django.urls import path, include
from rest_framework import routers

from applications.confirmation import viewsets

default_router = routers.DefaultRouter()
default_router.register(r'', viewsets.ConfirmationViewSet, 'registration')


urlpatterns = [
    path('', include(default_router.urls)),
]