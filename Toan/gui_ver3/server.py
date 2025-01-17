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
       def get(self):
              get_info1 = int(request.args.get('reqsv'))
              print('1233')
              res = None
              if get_info1 == 200:
                     res = {'respsv': get_info1, 'error': 0, 'data': ''}
              elif get_info1 == 201:
                     res = {'respsv': get_info1, 'error': 0, 'data': ''}
              elif get_info1 == 202:
                     res = {'respsv': get_info1, 'error': 0, 'data': self.dataAdruino()}
              else:
                     res = {'respsv': get_info1, 'error': 0, 'data': self.dataAdruino()}
              return jsonify(res)
       def dataAdruino(self):
              res = {
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
              return res;
              
api.add_resource(show_info, '/infos/') # Route_3


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=200)