from flask_restx import Namespace, Resource, reqparse
import random
import math
import datetime

api = Namespace('History', description='History data')

def getData():
    one_day = datetime.timedelta(days=1)
    # TODO: get data from database

    today = datetime.datetime.today()
    return [
        {
            'date': (today - datetime.timedelta(days=i)).timestamp(),
            'count': math.ceil(random.uniform(1, 100))
        } for i in range(10)
    ]

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

@api.route('/')
class HistoryData(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        id_ = args['id']

        return {
            'data': getData()
        }
