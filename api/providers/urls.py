# -*- coding: utf-8 -*-
"""Urls for resources."""

from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter

from . import views

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'provider', views.ProviderViewSet)
router.register(r'servicearea', views.ServiceAreaViewSet)


# Include the routes URLs
urlpatterns = [
    url(r'/', include(router.urls)),
]
