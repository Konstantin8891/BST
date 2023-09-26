from django.core.mail import EmailMessage
from django.db import models
from django.db.models import signals
from django.dispatch import receiver

from orders.models import Order


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)


@receiver(signals.post_save, sender=Robot)
def create_customer(sender, instance, created, **kwargs):
    robot_counter = Robot.objects.filter(serial=instance.serial).count()
    if robot_counter == 1:
        orders = Order.objects.filter(robot_serial=instance.serial)
        if orders.exists():
            for order in orders:
                customer = order.customer
                model, version = order.robot_serial.split('-')
                email = EmailMessage(
                    'New arrivals in stock',
                    'Добрый день!\n' +
                    'Недавно вы интересовались нашим роботом модели ' +
                    f'{model}, версии {version}.\n' +
                    'Этот робот теперь в наличии. Если вам подходит этот ' +
                    'вариант - пожалуйста, свяжитесь с нами',
                    to=[customer.email]
                )
                email.send()
