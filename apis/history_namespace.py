from flask_restx import Namespace, Resource, fields, reqparse
import random

api = Namespace('History', description='History data')


parser = reqparse.RequestParser()
parser.add_argument('start_date', type=str)
parser.add_argument('end_date', type=str)

@api.route('/<city>')
@api.param('city', 'The name of the city')
@api.expect(parser)
class HistoryData(Resource):
    def get(self, city):
        args = parser.parse_args()
        start_date = args['start_date']
        end_date = args['end_date']

        return {
            'start_date': start_date,
            'end_date': end_date,
            'city': city,
            'count': random.randint(10, 100)
        }
