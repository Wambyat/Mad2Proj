from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import time

app = Flask(__name__)
app.config.from_object(__name__)
# We are doing this to allow vue to send requests to this flask server.
CORS(app, resources={r"/*": {"origins": "*"}})


# This is just a testing route. Use this to run sanity tests and whatever else.
@app.route("/", methods=["GET","POST"])
def home():
    return jsonify({"message": "This is a test message. From Flask."})


@app.route("/model/", methods=["POST", "GET"])
def model():
    return jsonify({"data": "Model has been called! Hello from python"})


# This launches the flask server.
if __name__ == "__main__":
    # debug=True is used during development. It auto restarts the server when this file is modified.
    # app.run(debug=True)
    app.run(port=5000)
