from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем настройки Django по умолчанию для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal.settings')

app = Celery('newsportal')

# Загружаем настройки Django в Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит и регистрирует задачи из установленных приложений Django
app.autodiscover_tasks()
