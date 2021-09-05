""" This is a tutorial code for flask """

# import pdb
import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    ''' Function to call another api for computing SHA'''

    # return "Hello World"
#    if request.method == "POST":
#        first_name = request.form.get("fname")
#        last_name = request.form.get("lname")
#        return f"Your name is: {first_name} {last_name}"

#    pdb.set_trace()

    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        full_name = first_name + str(" ") + last_name

        # apiurl = "http://localhost:5001/SHA/" + full_name
        apiurl = "http://backend:5001/SHA/" + full_name
        print (f'Requesting to URL: {apiurl}')

        resp = requests.get(apiurl)
        print (resp.text)

        return f"Your HASH name is: {resp.json()['HashName']}"

    return render_template("index.html")

# app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000)))

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 5000)
