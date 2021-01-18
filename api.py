from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask_compress import Compress

app = Flask(__name__)
api = Api(app)
Compress(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

BASE_URL = '/v1/'

@app.route(BASE_URL + 'hello-world', methods=['GET'])
def helloWorld():
    print('GET Request - /v1/hello-world')
    return jsonify({'msg': 'Hello World'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
