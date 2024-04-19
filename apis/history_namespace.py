from flask_restx import Namespace, Resource, reqparse
import random
import math
import datetime
import pymongo
from urllib import parse

# 转义用户名和密码
user = parse.quote_plus("majingch")
passwd = parse.quote_plus("WS@mjc2000")

# 连接MongoDB
client = pymongo.MongoClient("mongodb+srv://{0}:{1}@578hw.1zxuyxd.mongodb.net/?retryWrites=true&w=majority&appName=578hw".format(user,passwd))

db = client["578backend"]
collection_history = db["history"]

api = Namespace('History', description='History data')

def getData(id):
    # one_day = datetime.timedelta(days=1)
    # TODO: get data from database
    # Define the query to find documents where "id" is equal to id_value
    query = {"id": id}

    # Define the projection to exclude the "_id" field
    projection = {"_id": 0}

    # Use the find method with the query and projection
    cursor = collection_history.find(query, projection)

    # Convert the cursor to a list of documents
    documents = list(cursor)

    return documents
    # today = datetime.datetime.today()
    # return [
    #     {
    #         'date': (today - datetime.timedelta(days=i)).timestamp(),
    #         'count': math.ceil(random.uniform(1, 100))
    #     } for i in range(10)
    # ]

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

@api.route('/')
class HistoryData(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        id_ = args['id']

        return {
            'data': getData(id_)
        }
