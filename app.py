from flask import Flask
from views import index

app = Flask(__name__)

app.register_blueprint(index.blueprint, url_prefix='/')

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0')
