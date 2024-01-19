from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/counter/', consumers.CounterConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
