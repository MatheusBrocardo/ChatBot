from services.waha import Waha
from database.redis import GerenciaSessao

GerenciaSessao = GerenciaSessao()

class GerenciaMensagem:
    def __init__(self,user_id,mensagem,step):
        self.user_id   = id_chat
        self.mensagem  = mensagem
        self.step      = step
        
    def analisa_mesagem(self,id_chat,mensagem):
        
        self.user_id   = id_chat
        self.mensagem  = mensagem
    
        # Verifica se te, sessão

