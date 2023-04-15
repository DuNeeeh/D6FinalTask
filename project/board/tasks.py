from celery import shared_task
from django.template.loader import render_to_string
from project.settings import DEFAULT_FROM_EMAIL
from simpleapp.models import *
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from simpleapp.models import News


@receiver(post_save, sender=News)
def product_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новая новость в категории {instance.category}!'

    text_content = (
        f'Новость: {instance.name}\n'
        f'Описание: {instance.description}\n\n'
        f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новость: {instance.name}<br>'
        f'Описание: {instance.description}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def new_post_notif(instance_id):
    instance = Post.objects.get(pk=instance_id)
    categories = instance.post_category.all()
    subscribers = []

    for category in categories:
        subscribers += category.subscribers.all()

    subscribers = list(set(sub.email for sub in subscribers))
    print(subscribers)

    for mail in subscribers:
        html_content = render_to_string(
            'new_post_created.html',
            {'text': instance.preview, 'link': "http://127.0.0.1:8000" f'/posts/{instance_id}'}
        )

        msg = EmailMultiAlternatives(
            subject=instance.title,
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[mail]
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()
