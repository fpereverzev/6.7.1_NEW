from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.models import DjangoJobExecution

def send_weekly_newsletter():
    # Ваша логика для отправки еженедельных рассылок
    print("Отправка еженедельной рассылки.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        send_weekly_newsletter,  # Используйте вашу функцию
        'cron',  # Тип триггера
        day_of_week='fri',  # День недели: пятница
        hour=18,  # Время: 18:00
        name='send_weekly_newsletter',  # Название задачи
        jobstore='default',  # Хранилище задач
        replace_existing=True,  # Заменить существующую задачу
    )

    register_events(scheduler)  # Регистрация событий (например, для логирования)
    scheduler.start()  # Запуск планировщика
    print("Планировщик запущен.")
