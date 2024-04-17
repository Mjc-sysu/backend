from flask_restx import Api

from .data_namespace import api as ns1
from .history_namespace import api as ns2
from .prediction_namespace import api as ns3

api = Api(
    title='Backend for PATROL',
    version='1.0',
    description='Backend for PATROL app',
)

api.add_namespace(ns1, path='/data')
api.add_namespace(ns2, path='/history')
api.add_namespace(ns3, path='/prediction')
