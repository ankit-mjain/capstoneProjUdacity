""" This is a code to compute SHA for any input """

import hashlib
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

@app.route('/', methods=['GET', 'POST'])

class SHA(Resource):
    """ Class to compute sha256 for any imput """

    def get(self, name):
        """ GET Function """

        print("Inside GET Function")
        print(f"Your name is: {name}")

        result = hashlib.sha256(name.encode())
        print(f"Your hash name is: {result.hexdigest()}")

        # return f"Your hash name is: {result.hexdigest()}"
        return jsonify({'HashName':result.hexdigest()})

    def post(self, name):
        """ POST Function """

        print("Inside POST Function")
        print(f"Your name is: {name}")

        result = hashlib.sha256(name.encode())
        print(f"Your hash name is: {result.hexdigest()}")

        # return f"Your hash name is: {result.hexdigest()}"
        return jsonify({'HashName':result.hexdigest()})

api.add_resource(SHA,'/SHA/<string:name>')

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port=5001)
