from django.shortcuts import render
from django.views import View
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import threading
from .utils import ListAppender
import time
import numpy as np

def home(request):
    context = {}
    return render(request, 'main.html', context)


class Counter(View):
    """
    A dummy example of the progress of a process. In this case, the progress
    of ListAppender
    """

    def __init__(self):
        self.m = []

    def get(self, request, *args, **kwargs):
        threading.Thread(
            target=self._threader_function,
            kwargs={'ls': range(10000000)}
        ).start()
        context = {}
        return render(request, 'base/counter.html', context)

    def post(self, request, *args, **kwargs):
        """
        dummy method. ony get is called in the view.
        """
        context = {}
        return render(request, 'main.html', context)

     
    def _threader_function(self, ls):
        ListAppender(m=self.m).appender(ls=ls, updater=self._async_to_sync)
        return None

    
    def _async_to_sync(self, i, total):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'counter_group', 
            {
                'type': 'counter.update',
                'current_count':f'%{np.round(100 * (i + 1) / total, 2)}',
                'total': total
            }
        )
