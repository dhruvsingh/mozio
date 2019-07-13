# -*- coding: utf-8 -*-
"""models for provider."""
from django.db import models
from django.contrib.gis.db import models as gis_models


class Provider(models.Model):
    """Store provider information."""

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    # this can be a FK to a master table for languages
    language = models.CharField(max_length=255, blank=True, null=True)
    # this can be a FK to a master table for currencies
    currency = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        """__repr__."""
        return "%s - %s" % (self.name, self.email)

    __str__ = __repr__


class ServiceArea(models.Model):
    """Store service area for a provider."""

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    provider = models.ForeignKey(
        Provider,
        null=True,
        blank=True,
        related_name="provider",
        on_delete=models.DO_NOTHING,
    )
    area = gis_models.MultiPolygonField()
