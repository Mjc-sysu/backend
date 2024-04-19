from flask_restx import Namespace, Resource, fields, reqparse
import time
import random
import pymongo
from urllib import parse

# 转义用户名和密码
user = parse.quote_plus("majingch")
passwd = parse.quote_plus("WS@mjc2000")

# 连接MongoDB
client = pymongo.MongoClient("mongodb+srv://{0}:{1}@578hw.1zxuyxd.mongodb.net/?retryWrites=true&w=majority&appName=578hw".format(user,passwd))


db = client["578backend"]
collection_data = db["data"]

def getData(longitude, latitude):
    # TODO: get data from database
    # return [
    #     {
    #         'id': i + 1,
    #         'latitude': latitude + random.uniform(-0.2, 0.2),
    #         'longitude': longitude + random.uniform(-0.2, 0.2),
    #         'source': random.choice(['X', 'user report', 'facebook']),
    #         'lastUpdated': time.time(),
    #     } for i in range(15)
    # ]
    projection = {"_id": 0}
     # Fetch all documents from the collection
    documents = collection_data.find({},projection = {"_id": 0})

    # Convert the cursor to a list of dictionaries
    document_list = list(documents)

    return document_list

def get_next_id(collection):
    # Find the document with the maximum id
    max_id_doc = collection_data.find_one({}, sort=[("id", pymongo.DESCENDING)], projection={"id": 1,"_id":0})

    if max_id_doc and "id" in max_id_doc:
        return int(max_id_doc["id"]) + 1
    else:
        return 1  # If no documents or no "id" field found, start from 1

def putData(data):
    # TODO put data in database
    next_id = get_next_id(collection_data)

    # Update the id in the report_data
    data["id"] = next_id

    # Insert the report_data into the collection
    collection_data.insert_one(data)
    data.pop('_id')
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

