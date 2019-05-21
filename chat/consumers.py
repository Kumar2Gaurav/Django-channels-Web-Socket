from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # import ipdb;
        # ipdb.set_trace()
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        count=1
        while count<10:
            self.send(text_data=json.dumps({
                'message': message}))
            count+=1