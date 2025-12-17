"""
Pytest configuration for Django tests
"""
import os
import django
from django.conf import settings
import pytest

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectmanagerdashboard.settings')

def pytest_configure(config):
    """Configure pytest for Django"""
    if not settings.configured:
        django.setup()

@pytest.fixture(scope='session')
def django_db_setup():
    """Ensure database migrations are applied before tests"""
    from django.core.management import call_command
    call_command('migrate', '--noinput')
