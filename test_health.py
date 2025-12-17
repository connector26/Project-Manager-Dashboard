"""
Basic health check tests for the Project Manager Dashboard
"""
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
class TestHealthCheck:
    """Test the health check endpoint"""
    
    def test_healthz_endpoint(self):
        """Test that the healthz endpoint returns 200 OK"""
        client = Client()
        response = client.get('/healthz/')
        assert response.status_code == 200
        assert b'OK' in response.content
