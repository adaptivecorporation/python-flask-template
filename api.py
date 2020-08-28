from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask_compress import Compress
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
Compress(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
auth = HTTPBasicAuth()

USER_DATA = {
    "api":"apikey"
}

BASE_URL = '/v1/'


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
