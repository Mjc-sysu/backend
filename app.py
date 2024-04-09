from flask import Flask
from apis import api

app = Flask(__name__)
api.init_app(app)

app.config['RESTPLUS_MASK_SWAGGER'] = False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
