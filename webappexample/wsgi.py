import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webappexample.settings")

application = get_wsgi_application()
app = application  # 或者 handler = application

