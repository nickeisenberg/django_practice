from django.shortcuts import render
from django.views import View
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import threading


def home(request):
    context = {}
    return render(request, 'main.html', context)


class Counter(View):
    def __init__(self):
        self.m = []

    def get(self, request, *args, **kwargs):
        threading.Thread(
            target=self._update_counter,
            kwargs={'ls': range(100000000), "django_updater": True}
        ).start()
        context = {}
        return render(request, 'base/counter.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, 'main.html', context)

    def _update_counter(self, ls):
        then = time.time()
        for i, l in enumerate(ls):
            now = time.time()

            self.m.append(l)

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
