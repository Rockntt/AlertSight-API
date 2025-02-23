from flask_restful import Resource

class Ping(Resource):
    def get(self):
        return {'status': 'ok'}

class LastEvent(Resource):
    def get(self):
        return {'data': 'last_accident'}
class Upload(Resource):
    def post(self):
        return {'status': 'recieved'}

class Fetch(Resource):
    def get(self, id):
        return {'data': 'data-{}'.format(id)}