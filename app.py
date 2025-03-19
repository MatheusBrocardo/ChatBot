from flask import Flask
from routes import webhook
from database.redis import GerenciaSessao

# Instanciando o Flask
app = Flask(__name__)

# Instanciando as rotas
app.register_blueprint(webhook.hook)

if __name__ == '__main__':
    # Inciando a aplicação
    GerenciaSessao.monitora_sessoes()
    app.run(debug=True,host='0.0.0.0',port=5000)
