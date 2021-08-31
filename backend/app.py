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

#def index():
#    # return "Hello World"
#    if request.method == "POST":
#        first_name = request.form.get("fname")
#        last_name = request.form.get("lname")
#        full_name = first_name + last_name
#
#        result = hashlib.sha256(full_name.encode())
#        print(result.hexdigest())
#
#        return f"Your hash name is: {result.hexdigest()}"

#    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
