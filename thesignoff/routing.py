from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path

from user import consumer

websocket_urlpattern = [
    path('ws/tshirtroom/<str:slug>', consumer.TshirtConsumer)
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpattern))
})