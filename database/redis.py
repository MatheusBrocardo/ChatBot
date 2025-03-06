import redis
import threading

redis_client = redis.Redis(host='redis', port=6379, db=0,decode_responses=True)

class GerenciaSessao:
    
    def __init__(self,host='redis',port=6379,db=0,session_timeout=3000):
        self.redis_client = redis.Redis(host=host, port=port, db=db,decode_responses=True)
        self.session_timeout = session_timeout

    def cria_sessao(self,chat_id,step):
        chat_id = f"user:{chat_id}"
        self.redis_client.hmset(chat_id,{
            "status":"ativo",
            "step": step
            })
        self.redis_client.expire(chat_id,self.session_timeout)
        
    def renova_sessao(self,chat_id,step):
        chat_id = f"user:{chat_id}"
        if self.redis_client.exists(chat_id):
            self.redis_client.expire(chat_id,self.session_timeout)
            return True
        return False

    def verifica_sessao(self,chat_id):
        chat_id = f"user:{chat_id}"
        session_data = self.redis_client.hgetall(chat_id)
        if not session_data:
            return False
        return True

    def altera_step_sessao(self,chat_id,new_step):
        chat_id = f"user:{chat_id}"
        self.redis_client.hset(chat_id,"step",new_step)
    
    def encerra_sessao(self,chat_id):
        chat_id = f"user:{chat_id}"
        self.redis_client.delete(chat_id)
    
    def monitora_sessoes(self):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe("__keyevent@0__:expired")

        for message in pubsub.listen():
            if message["type"] == "message":
                chat_id = message["data"]
                self.redis_client.delete(chat_id)