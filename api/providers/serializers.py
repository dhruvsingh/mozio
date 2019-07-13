# -*- coding: utf-8 -*-
"""Serializers for provider app."""

from rest_framework import serializers

from .models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer class for Provider model."""

    class Meta:
        """Meta for ProviderSerializer."""

        model = Provider
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'language',
            'currency',
        )
        read_only_fields = ('id',)


class ServiceAreaSerializer(serializers.ModelSerializer):
    """Serializer class for ServiceArea model."""

    class Meta:
        """Meta for ServiceAreaSerializer."""

        model = ServiceArea
        fields = (
            'id',
            'name',
            'price',
            'provider',
            'area',
        )
        read_only_fields = ('id',)
