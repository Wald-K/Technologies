import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
# namespace musi byc aby wiedziec w pliku settings ktore ustawienia dotycza Celery

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
