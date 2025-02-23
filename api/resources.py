from flask_restful import Resource, reqparse
from flask import current_app, request
from api.models.Accident import Accident, db
import os
from datetime import datetime
from utils import filename_generator

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True, help='Type is required')
parser.add_argument('source_id', type=int, required=True, help='Source ID is required')

class Ping(Resource):
    def get(self):
        return {'status': 'ok'}

class LastEvent(Resource):
    def get(self):
        return {'data': 'last_accident'}

class Upload(Resource):
    def post(self):
        type_ = request.form.get('type')
        source_id = request.form.get('source_id')
        image = request.files.get('image')
        date = datetime.now()

        if 'image' not in request.files:
            return {'error': 'No image file provided'}, 400

        file = request.files['image']

        if file.filename == '':
            return {'error': 'No selected file'}, 400

        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename_generator(file.filename[-3:]))
        file.save(file_path)

        new_accident = Accident(
            type=type_,
            source_id=source_id,
            date=date,
            image=file_path
        )
        db.session.add(new_accident)
        db.session.commit()

        return {'message': 'Accident saved'}, 201

class Fetch(Resource):
    def get(self, id):
        return {'data': 'data-{}'.format(id)}