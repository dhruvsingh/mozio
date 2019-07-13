# -*- coding: utf-8 -*-
"""Serializers for provider app."""

from rest_framework import serializers

from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer class for Resource model."""

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
