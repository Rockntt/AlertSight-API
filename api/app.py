from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources import *
from api.models.Accident import db

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alertsight.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

db.init_app(app)

api.add_resource(Ping, '/ping')
api.add_resource(Upload, '/upload')
api.add_resource(LastEvent, '/last_event')
api.add_resource(Fetch, '/fetch/<int:id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)