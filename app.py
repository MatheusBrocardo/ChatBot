from flask import Flask
from routes import webhook

# Instanciando o Flask
app = Flask(__name__)

# Instanciando as rotas
app.register_blueprint(webhook.hook)

if __name__ == '__main__':
    # Inciando a aplicação
    app.run(debug=True,host='0.0.0.0',port=5000)
