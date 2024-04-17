from flask_restx import Namespace, Resource, fields, reqparse
import time
import random

def getData(longitude, latitude):
    # TODO: get data from database
    return [
        {
            'id': i + 1,
            'latitude': latitude + random.uniform(-0.2, 0.2),
            'longitude': longitude + random.uniform(-0.2, 0.2),
            'source': random.choice(['X', 'user report', 'facebook']),
            'lastUpdated': time.time(),
        } for i in range(15)
    ]

def putData(data):
    # TODO put data in database
    pass


api = Namespace('data', description='get data and report data')

get_parser = reqparse.RequestParser()
get_parser.add_argument('longitude', type=float)
get_parser.add_argument('latitude', type=float)

post_parser = reqparse.RequestParser()
post_parser.add_argument('longitude', type=float)
post_parser.add_argument('latitude', type=float)
post_parser.add_argument('status', type=str)


@api.route('/')
@api.doc('Get list of data')
class Data(Resource):
    @api.expect(get_parser)
    def get(self):
        args = get_parser.parse_args()
        longitude = args['longitude']
        latitude = args['latitude']

        return {
            'data': getData(longitude, latitude),
        }


    @api.expect(post_parser)
    def post(self):
        args = get_parser.parse_args()
        longitude = args['longitude']
        latitude = args['latitude']

        report_data = {
            'id': 1,
            'longitude': longitude,
            'latitude': latitude,
            'source': 'user report',
        }

        putData(report_data)

        return {
            'message': 'data added to database',
            'data': report_data
        }

