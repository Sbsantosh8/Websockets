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







from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json


class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "global_chat"  # Fixed room name for simplicity

        # Join group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        await self.send(text_data="🟢 Connected to group chat.")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")

        # Send message to group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from group and send to WebSocket
    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=f"Broadcast: {message}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
