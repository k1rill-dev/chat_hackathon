import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chats.models import ChatModel


# from .AES import Aes

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        message = data['message']
        username = data['username']
        type_msg = data['type_msg']

        await self.save_message(username, self.room_group_name, message, type_msg)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'type_msg': type_msg,
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        print(event)
        message = event['message']
        username = event['username']
        type_msg = event['type_msg']

        await self.send(text_data=json.dumps({
            'message': message,
            'type_msg': type_msg,
            'username': username
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_message(self, username, thread_name, message, type_msg):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name, type_msg=type_msg)


class NotifyNewMessage(AsyncWebsocketConsumer):
    async def connect(self):
        # my_id = self.scope['user'].id
        # other_user_id = self.scope['url_route']['kwargs']['id']
        # if int(my_id) > int(other_user_id):
        #     self.room_name = f'{my_id}-{other_user_id}'
        # else:
        #     self.room_name = f'{other_user_id}-{my_id}'

        # self.room_group_name = 'chat_%s' % self.room_name
        #
        # await self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )

        await self.accept()

    # async def receive(self, text_data=None, bytes_data=None):
    #     data = json.loads(text_data)
    #
    #     message = data['message']
    #     username = data['username']
    #     type_msg = data['type_msg']
    #
    #     await self.save_message(username, self.room_group_name, message, type_msg)
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'type_msg': type_msg,
    #             'message': message,
    #             'username': username,
    #         }
    #     )
    #
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        type_msg = event['type_msg']

        await self.send(text_data=json.dumps({
            'message': message,
            'type_msg': type_msg,
            'username': username
        }))
    #
    # async def disconnect(self, code):
    #     self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )
    #
    @database_sync_to_async
    def get_num_msg(self, username, thread_name, message, type_msg):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name, type_msg=type_msg)
