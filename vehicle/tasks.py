from celery import shared_task
from django.core.mail import send_mail

from vehicle.models import Moto, Car


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print('Неверный пробег')
                    break


def check_filter():
    filter_price = {'price--lte': 500}

    if Car.objects.fiter(**filter_price).exists():
        send_mail(
            subject='Отчёт по фильтру',
            message='У нас есть машины под ваш фильтрб заходите на сайи',
            from_email='admin@admin.com',
            recipient_list=['user@user.com'],
        )

