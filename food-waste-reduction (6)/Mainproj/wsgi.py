"""
WSGI config for Mainproj project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mainproj.settings')
application = get_wsgi_application()
