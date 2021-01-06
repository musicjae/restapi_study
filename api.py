from flask_restful import Resource
from flask_restful import reqparse

class Plus(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('x', required=True, type=int, help='x cannot be blank')
            parser.add_argument('y', required=True, type=int, help='y cannot be blank')
            parser.add_argument('z',required=True,type=int)
            args = parser.parse_args()
            result = args['x'] + args['y'] + args['z']
            return {'result': result}
        except Exception as e:
            return {'error': str(e)}

from flask import Flask
from flask_restful import Api

app = Flask('My First App')
api = Api(app)
api.add_resource(Plus, '/plus')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000, debug=True)