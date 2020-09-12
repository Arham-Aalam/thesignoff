from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TshirtConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname = self.scope['url_route']['kwargs']['slug']

        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # await self.disconnect()
        pass

    async def receive(self, text_data):
        print('>>>>', text_data)