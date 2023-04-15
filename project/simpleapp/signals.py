from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import News
from board.tasks import new_post_notif


@receiver(m2m_changed, sender=News)
def notification_for_news(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        new_post_notif.delay(instance.id)
