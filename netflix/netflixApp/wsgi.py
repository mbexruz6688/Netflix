import os, django

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netflix.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'netflix.settings'
django.setup()
application = get_wsgi_application()