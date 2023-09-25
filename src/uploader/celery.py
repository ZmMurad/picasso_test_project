# celery.py

from __future__ import absolute_import, unicode_literals
import logging
import os
from celery import Celery

# Установите переменную окружения DJANGO_SETTINGS_MODULE в настройках проекта Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uploader.settings')

app = Celery('uploader')

# Загрузка настроек Celery из настроек Django.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True
# Автоматическая обнаружение и регистрация задач из приложений Django.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    logging.warning('Request: {0!r}'.format(self.request))