# -*- coding: utf-8 -*-
"""Views for provider."""
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Provider
from .serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """Provider viewset for CUD operations on provider model."""

    model = Provider
    pagination_class = PageNumberPagination
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
