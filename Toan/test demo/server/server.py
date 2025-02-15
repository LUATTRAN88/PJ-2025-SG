from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from sqlalchemy import create_engine
from json import dumps
# import mysql.connector
import random
import json
import serialport as ard
import extend as ext
# from flask.ext.jsonpify import jsonify
aruidno = ard.Arduino();
aruidno.connect_port();
app = Flask(__name__)
api = Api(app)

class show_info(Resource):
       def get(self):
              reqsv = int(request.args.get('reqsv'))
              res = ""
              if reqsv == 20000:
                     port = int(request.args.get('port'))
                     status = int(request.args.get('status'))
                     print(port)
                     print(status)
                     #aruidno.write_port(port,status)
              elif reqsv == 20001:
                     res = {'respsv': reqsv, 'error': 0, 'data': ''}
              elif reqsv == 20002:
                     res = self.dataAdruino()
              else:
                     res =  self.dataAdruino()
              return jsonify(res)
       def dataAdruino(self):
              y = json.loads(aruidno.store_data)
              return y;
              
api.add_resource(show_info, '/infos/') # Route_3


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=200)