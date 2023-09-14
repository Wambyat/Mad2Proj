from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity, verify_jwt_in_request, decode_token
import datetime
import time

app = Flask(__name__)
app.config.from_object(__name__)
app.config["JWT_SECRET_KEY"] = "WOWamzingSecretuWu"
jwt = JWTManager(app)
# We are doing this to allow vue to send requests to this flask server.
CORS(app, resources={r"/*": {"origins": "*"}})
access_token = ""

# This is just a testing route. Use this to run sanity tests and whatever else.
@app.route("/", methods=["GET","POST"])
def home():
    return jsonify({"message": "This is a test message. From Flask."})

@app.route("/auth", methods=["GET"])
def auth():
    global access_token
    access_token = create_access_token(identity="test")
    time.sleep(2)
    return jsonify({"access_token": access_token,"message": "You are authed now try visiting /testok and /testnotok"})

@app.route("/testok", methods=["GET"])
@jwt_required()
def testok():
    curr = get_jwt_identity()
    if curr == "test":
        return jsonify({"message": "You are authorized"})
    return jsonify({"message": "You are not authorized"})

@app.route("/testnotok", methods=["GET"])
@jwt_required()
def testnotok():
    curr = get_jwt_identity()
    if curr == "test":
        return jsonify({"message": "You are not authorized"})


@app.route("/model/", methods=["POST", "GET"])
def model():
    return jsonify({"data": "Model has been called! Hello from python"})


# This launches the flask server.
if __name__ == "__main__":
    # debug=True is used during development. It auto restarts the server when this file is modified.
    app.run(debug=True)
    # app.run(port=5000)
