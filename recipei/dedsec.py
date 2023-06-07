from flask import Flask, request

app = Flask(__name__)

@app.before_request
def verificar_seguranca():
    # Verificar se a requisição é segura (HTTPS)
    if not request.is_secure and app.env == "production":
        return "Acesso não seguro. Use HTTPS para acessar este site.", 403

    # Adicione outras verificações de segurança aqui, conforme necessário
    # Por exemplo, verificação de token, autenticação de usuário, etc.
    app.run(ssl_context='adhoc')


    # Se todas as verificações de segurança passarem, permita a continuação da requisição
    return None

@app.route('https://recipei.netlify.app/')
def index():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run()
