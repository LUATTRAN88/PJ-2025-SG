from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from sqlalchemy import create_engine
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
              if get_info1 == 20000:
                     res = {'respsv': get_info1, 'error': 0, 'data': ''}
              elif get_info1 == 20001:
                     res = {'respsv': get_info1, 'error': 0, 'data': ''}
              elif get_info1 == 20002:
                     res = {'respsv': get_info1, 'error': 0, 'data': self.dataAdruino()}
              else:
                     res = {'respsv': get_info1, 'error': 0, 'data': self.dataAdruino()}
              return jsonify(res)
       def dataAdruino(self):
              res = {
                     'vln1': round(random.uniform(1.0, 50.0),2), 
                     'vln2': round(random.uniform(1.0, 50.0),2),
                     'vln3': round(random.uniform(1.0, 50.0),2),
                     'cur1': round(random.uniform(1.0, 50.0),2),
                     'cur2': round(random.uniform(1.0, 50.0),2),
                     'cur3': round(random.uniform(1.0, 50.0),2),
                     'kw1': round(random.uniform(1.0, 50.0),2),
                     'kw2': round(random.uniform(1.0, 50.0),2),
                     'kw3': round(random.uniform(1.0, 50.0),2), 
                     'pf1': round(random.uniform(1.0, 50.0),2), 
                     'pf2': round(random.uniform(1.0, 50.0),2), 
                     'pf3': round(random.uniform(1.0, 50.0),2), 
                     'rl': [
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                     ],
                     'rl_power':[
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            {'val':round(random.uniform(1.0, 50.0),1), 'on':random.randint(0,1)},
                            ],
                     'freq': round(random.uniform(1.0, 50.0),2),
                     'tkw': round(random.uniform(1.0, 50.0),2),
                     'v12': round(random.uniform(1.0, 50.0),2),
                     'v23': round(random.uniform(1.0, 50.0),2),
                     'v31': round(random.uniform(1.0, 50.0),2),
                     'tempc': round(random.uniform(1.0, 50.0),2),
                     }
              return res;
              
api.add_resource(show_info, '/infos/') # Route_3


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=200)