"""
WSGI config for streaming_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Define o módulo de configurações padrão utilizado pelo Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'streaming_platform.settings')

# Cria a aplicação WSGI utilizada por servidores web compatíveis
application = get_wsgi_application()