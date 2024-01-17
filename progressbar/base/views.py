from django.shortcuts import render
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import threading

def home(request):
    context = {}
    return render(request, 'main.html', context)


def counter(request):
    threading.Thread(target=update_counter).start()
    context = {}
    return render(request, 'base/counter.html', context)

def update_counter():
    channel_layer = get_channel_layer()
    for i in range(10):
        x = i + 1
        async_to_sync(channel_layer.group_send)('counter_group', {
            'type': 'counter.update',
            'message': x
        })
        time.sleep(1)  # Simulate work being done
