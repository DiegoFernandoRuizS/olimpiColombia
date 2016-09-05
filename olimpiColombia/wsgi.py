import os

import newrelic.agent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

newrelic.agent.initialize('newrelic.ini')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "olimpiColombia.settings")

application = get_wsgi_application()
application = newrelic.agent.wsgi_application()(application)
