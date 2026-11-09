from flask import Flask, render_template, request, jsonify
from answers import FAQ, answer_message

faq = FAQ


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 4096

    @app.get('/')
    def index():
        return render_template('index.html')

    @app.post('/chat')
    def chat():
        if not request.is_json:
            return jsonify(error='Envie um objeto JSON com a mensagem.'), 415
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify(error='Envie um objeto JSON com a mensagem.'), 400
        try:
            return jsonify(response=answer_message(payload.get('message')))
        except ValueError as error:
            return jsonify(error=str(error)), 400

    @app.errorhandler(413)
    def too_large(_error):
        return jsonify(error='A requisição excede o limite permitido.'), 413

    @app.after_request
    def response_headers(response):
        response.headers['Cache-Control'] = 'no-store'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'"
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False)
