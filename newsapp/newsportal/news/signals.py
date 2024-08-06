# signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post, Subscriber
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

@receiver(m2m_changed, sender=Post.postCategory.through)
def notify_subscribers(sender, instance, action, **kwargs):
    if action == 'post_add':
        categories = instance.postCategory.all()
        subscribers = set()
        for category in categories:
            subscribers.update(category.subscriber_set.values_list('user__email', flat=True))
        if subscribers:
            subject = f"New post in category {', '.join([category.name for category in categories])}"
            message = render_to_string('new_post_email.html', {'post': instance})
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, list(subscribers))
