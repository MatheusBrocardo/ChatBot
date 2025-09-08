
from flask import Blueprint,jsonify,request
from bot.bot import GerenciaMensagem
import time,random

hook = Blueprint('hook', __name__)

@hook.route('/chatbot/webhook/', methods=['POST'])
def webhook():

    # Pega os dados da requisição
    data = request.json

    # Pega o id do chat enviado na requisição/Conteudo da mensagem
    chat_id = data['payload']['from']
    received_message = data['payload']['body']

    # Vefifica se a mensagem é de um grupo ou status
    is_group = 'g.us' in chat_id
    is_status = 'status@broadcast' in chat_id

    # Caso seja um grupo ou status, retorna um status de sucesso, sem enviar retorno
    if is_group or is_status:
        return jsonify({'status':'success'}),200

    # Create an instance of GerenciaMensagem with the required arguments
    gerencia_mensagem = GerenciaMensagem(chat_id=chat_id, mensagem=received_message)

    # Process the received message
    gerencia_mensagem.recebe_mensagem(chat_id=chat_id, mensagem=received_message)
        
    return jsonify({'status': 'success'}), 200

# @hook.route('/chatbot/webhook/aimessage', methods=['POST'])
# def webhook():

#     waha = Waha()
#     bot  = AIBot()

#     data = request.json

#     chat_id = data['payload']['from']
#     received_message = data['payload']['body']

#     is_group = 'g.us' in chat_id
#     is_status = 'status@broadcast' in chat_id

#     if is_group or is_status:
#         return jsonify({'status':'success'}),200
        
#     waha.start_typing(chat_id=chat_id)

#     history_messages = waha.get_history_messages(
#         chat_id=chat_id,
#         limit=1,
#     )

#     response_message = bot.invoke(
#         history_messages=history_messages,
#         question=received_message,
#     )

#     waha.send_message(
#         chat_id=chat_id,
#         message=response_message,
#     )

#     waha.stop_typing(chat_id=chat_id)

#     return jsonify({'status': 'success'}), 200