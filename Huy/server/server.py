from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
# import mysql.connector
import random
# from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class show_info(Resource):
    def get(self, info):
        # cursor.execute("select * from room_system.user u where u.id =%s " ,(int(user_id),))
        # res = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in cursor.fetchone()]}
        # rand = 
        res = {'info': {
                'v1n': random.uniform(1.0, 50.0), 
               'v2n': random.uniform(1.0, 50.0),
               'v3n': random.uniform(1.0, 50.0),
               'i1': random.uniform(1.0, 50.0),
               'i2': random.uniform(1.0, 50.0),
               'i3': random.uniform(1.0, 50.0),
               'kw1': random.uniform(1.0, 50.0),
               'kw2': random.uniform(1.0, 50.0),
               'kw3': random.uniform(1.0, 50.0), 
               'pf1': random.uniform(1.0, 50.0), 
               'pf2': random.uniform(1.0, 50.0), 
               'pf3': random.uniform(1.0, 50.0), 
               'rl1': random.randint(0, 1),
               'rl2': random.randint(0, 1),
               'rl3': random.randint(0, 1),
               'rl4': random.randint(0, 1),
               'rl5': random.randint(0, 1),
               'rl6': random.randint(0, 1),
               'rl7': random.randint(0, 1),
               'rl8': random.randint(0, 1),
               'rl9': random.randint(0, 1),
               'rl10': random.randint(0, 1),
               'rl11': random.randint(0, 1),
               'rl12': random.randint(0, 1),
               'freq': random.uniform(1.0, 50.0),
               'tkw':random.uniform(1.0, 50.0)
        }
               }
        return jsonify(res)

api.add_resource(show_info, '/infos/<info>') # Route_3

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=200)
