#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


from channels import route
from channels import Group


# # This function will display all messages received in the console
# def message_handler(message):
#     # Accept the incoming connection
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })
#     # Add them to the chat group
#     Group().add(message.reply_channel)
#
#
# channel_routing = [
#     route("websocket.receive", message_handler)  # we register our message handler
# ]


from channels.routing import route
from channels_app.consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]