from django.shortcuts import render
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import threading


def home(request):
    context = {}
    return render(request, 'main.html', context)


def counter(request):
    threading.Thread(
        target=update_counter,
        kwargs={'ls': range(100000000), "django_updater": True}
    ).start()
    context = {}
    return render(request, 'base/counter.html', context)


def update_counter_():
    channel_layer = get_channel_layer()

    then = time.time()
    for x in range(100000000):
        now = time.time()
        if now - then > 1:
            then = now
            async_to_sync(channel_layer.group_send)(
                'counter_group', 
                {
                    'type': 'counter.update',
                    'current_count': x,
                    'total': 100000000
                }
            )
        elif x == 100000000 - 1:
            async_to_sync(channel_layer.group_send)(
                'counter_group', 
                {
                    'type': 'counter.update',
                    'current_count': x + 1,
                    'total': 100000000
                }
            )


def update_counter(ls, django_updater):

    m = []

    then = time.time()
    for i, l in enumerate(ls):
        now = time.time()
        m.append(l)

        if django_updater:
            if now - then > 1:
                then = now
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    'counter_group', 
                    {
                        'type': 'counter.update',
                        'current_count': i + 1,
                        'total': 100000000
                    }
                )
