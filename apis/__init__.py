from flask_restx import Api

from .history_namespace import api as ns1

api = Api(
    title='Backend for PATROL',
    version='1.0',
    description='Backend for PATROL app',
)

api.add_namespace(ns1, path='/history')
