# apps.py
from django.apps import AppConfig



class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        import news.signals  # Ensure the signals are registered

        from .tasks import start_scheduler
        start_scheduler()
