from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path("ws/wsc/", consumers.MyWebsocketConsumer.as_asgi()),
    path("async/", consumers.AsyncEchoConsumer.as_asgi()),
    path("ws/chat/", consumers.AsyncChatConsumer.as_asgi()),
]
