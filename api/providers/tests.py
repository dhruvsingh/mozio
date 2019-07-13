# -*- coding: utf-8 -*-
"""tests for provider class."""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Provider


class AccountTests(APITestCase):
    """Test cases for provider."""

    def setUp(self):
        """Called before each test case is executed."""
        data = {'name': 'Dhruv', 'email': 'dhruvsingh.er@gmail.com'}
        self.provider = Provider.objects.create(**data)

    def test_create_provider(self):
        """Ensure we can create a new provider."""
        url = reverse('provider-list')
        data = {'name': 'Dhruv', 'email': 'dhruvsingh.er@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 2)
        self.assertEqual(Provider.objects.last().name, data['name'])
