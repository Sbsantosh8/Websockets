# Topic -> Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("websocket connected...")
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Message Recieved from client...", text_data)

        self.send(text_data=f"Server says: {text_data.upper()}")

    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)


from channels.generic.websocket import AsyncWebsocketConsumer
import json


class AsyncEchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="WebSocket connected asynchronously!")

    async def receive(self, text_data):
        await self.send(text_data=f"You said (async): {text_data}")

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")
