import requests

class Waha:
    def __init__(self):
        self.url = 'http://waha:3000'

    def send_message(self,chat_id,message):
        url = f'{self.url}/api/sendText'

        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'session':'default',
            'chatId': chat_id,
            'text': message
        }

        requests.post(
            url=url,
            headers=headers,
            json=payload
        )
    
    def start_typing(self,chat_id):
        url = f'{self.url}/api/startTyping'

        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'session':'default',
            'chatId': chat_id
        }

        requests.post(
            url=url,
            headers=headers,
            json=payload
        )
    
    def stop_typing(self, chat_id):
        url = f'{self.url}/api/stopTyping'
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers,
        )

    def send_button(self,chat_id):
        url = f'{self.url}/api/sendButtons'

        headers = {
            'Content-Type': 'application/json',
        }

        payload = {
            'chatId': chat_id,
            'header': 'Escolha uma opção',
            'body':  'Lista de opções disponiveis',
            'footer': 'Em caso de duvidas, entre em contato em (19)3571-7500',
            'buttons': [
                {
                    'type': 'copy',
                    "text": "Copy code",
                    "copyCode": "4321"
                },
                {
                    "type": "call",
                    "text": "Call us",
                    "phoneNumber": "+1234567890"
                }
        ],
            'session': 'default'
        }

        requests.post(
            url=url,
            json=payload,
            headers=headers
        )
    
    def get_history_messages(self,chat_id,limit):
        
        url = f'{self.url}/api/default/chats/{chat_id}/messages?limit={limit}&downloadMedia=false'

        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(
            url=url,
            headers=headers,
        )
        return response.json()