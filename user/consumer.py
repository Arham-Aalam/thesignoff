from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core import serializers

from .models import *

import json

class TshirtConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname = self.scope['url_route']['kwargs']['slug']

        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        await self.accept()
        print('Connected!!')

    async def disconnect(self, close_code):
        # await self.disconnect()
        if self.groupname:
            await self.channel_layer.group_discard(
                self.groupname,
                self.channel_name
            )
            print('Disconnected!!')

    async def receive(self, text_data, bytes_data=None):
        print('>>>>', text_data)
        obj = json.loads(text_data)
        
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'broadcast',
                'coords': obj
            }
        )
    
    async def broadcast(self, event):
        if event['job'] == 'clear':
            # clear all coords from database
            self.clear_points(json.dumps(event))
        else:
            self.insert_coords(json.dumps(event))
        
        txt_data = json.dumps(self.get_friends(event))
        await self.send(text_data=txt_data)
    
    @database_sync_to_async
    def get_friends(self, data):
        trid = data['trid']
        tr = TshirtRoom(id=trid)

        frds = Friend.objects.filter(tshirt=tr)
        return serializers.serialize('json', frds)

    @database_sync_to_async
    def clear_points(self, data):
        fid = data[id]
        friend = Friend.objects.get(id=pid)

        friend.key_points = json.dumps([])
        friend.save()

    @database_sync_to_async
    def insert_coords(self, data):
        fid = data[id]
        friend = Friend.objects.get(id=pid)
        pdata = friend.key_points

        pdata = json.loads(pdata)
        for p in data['coords']:
            pdata.append(p)

        friend.color = data['color']
        friend.key_points = json.dumps(pdata)
        friend.save()