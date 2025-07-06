# Topic -> Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("websocket connected...")

    def receive(self, text_data=None, bytes_data=None):
        print("Message Recieved from client...", text_data)

    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
