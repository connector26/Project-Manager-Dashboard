"""
Pytest configuration for Django tests
"""
import os
import django
from django.conf import settings

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectmanagerdashboard.settings')

def pytest_configure(config):
    """Configure pytest for Django"""
    if not settings.configured:
        django.setup()
