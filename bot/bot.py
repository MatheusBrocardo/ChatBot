from services.waha import Waha
from database.redis import GerenciaSessao
import random,time

class GerenciaMensagem:
    def __init__(self, chat_id, mensagem):
        self.chat_id = chat_id
        self.mensagem_recebida = mensagem  # Renamed to avoid conflict
        self.step = 1
        self.GerenciaSessao = GerenciaSessao()
        self.waha = Waha()

    def recebe_mensagem(self, chat_id, mensagem):
        self.mensagem_recebida = mensagem
        self.user_id = chat_id

        self.GerenciaSessao.encerra_sessao(self.chat_id)

        if not self.GerenciaSessao.verifica_sessao(self.chat_id):
            self.step = 1
            self.GerenciaSessao.cria_sessao(self.chat_id, self.step)
            self.waha.start_typing(chat_id=self.chat_id)
            # self.waha.send_message(chat_id=self.chat_id, message=self.get_message("iteracao", "menu"))
            self.waha.send_message(chat_id=self.chat_id, message=self.get_message("iteracao", "opcoes"))
            return
        
    def get_message(self, contexto, step):  # Renamed method
        message = {
            "iteracao": {
                "bemvindo": "Olá seja bem-vindo ao nosso chatbot!",
                "menu": "Escolha uma opção:",
                "opcoes": "1 - Rastreamento",
                "sair": "Obrigado por usar o chatbot. Até logo!",
                "tracking": "Digite o numero da nota ficasl",
            },
            "sessao": {
                "expired": "Sua sessão expirou. Envie uma nova mensagem para recomeçar."
            },
            "erro": {
                "generico": "Desculpe, ocorreu um erro. Tente novamente mais tarde."
            }
        }
        return message[contexto][step]


