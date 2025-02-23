from flask import Flask
from flask_restful import Api
from resources import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Ping, '/ping')
api.add_resource(Upload, '/upload')
api.add_resource(LastEvent, '/last_event')
api.add_resource(Fetch, '/fetch/<int:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)