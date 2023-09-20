from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from flask_jwt_extended import (
    create_access_token,
    JWTManager,
    jwt_required,
    get_jwt_identity,
    verify_jwt_in_request,
    decode_token,
)
import datetime
import time

app = Flask(__name__)
app.config.from_object(__name__)
app.config["JWT_SECRET_KEY"] = "WOWamzingSecretuWu"
jwt = JWTManager(app)
# We are doing this to allow vue to send requests to this flask server.
CORS(app, resources={r"/*": {"origins": "*"}})
access_token = ""


def SQL(query):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query)
    output = c.fetchall()
    conn.commit()
    conn.close()
    return output


# This is just a testing route. Use this to run sanity tests and whatever else.
@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify({"message": "This is a test message. From Flask."})


@app.route("/test/", methods=["GET","POST"])
@jwt_required()
def test():
    print("hey?")
    global access_token
    return jsonify(
        {
            "access_token": access_token,
            "message": "You have sent it correctly!",
        }
    )


@app.route("/login", methods=["POST"])
def login():
    global access_token
    username = request.json.get("username")
    password = request.json.get("password")
    res = SQL("SELECT * FROM users")
    print(res)
    for i in res:
        if i[1] == username and i[2] == password:
            access_token = create_access_token(identity=i[0])
            print("holy authed baby")
            res = SQL("SELECT id FROM admin")
            if i[0] in res[0]:
                return jsonify(
                    {
                        "access_token": access_token,
                        "message": "You are logged in now",
                        "admin": True,
                    }
                )
            return jsonify(
                {"access_token": access_token, "message": "You are logged in now"}
            )
    return jsonify({"error": "Invalid username or password"})


# Reset access token
@app.route("/logout", methods=["GET"])
def reset():
    global access_token
    access_token = ""
    return jsonify({"message": "Access token has been reset"})


@app.route("/model/", methods=["POST", "GET"])
def model():
    return jsonify({"data": "Model has been called! Hello from python"})


# This launches the flask server.
if __name__ == "__main__":
    # debug=True is used during development. It auto restarts the server when this file is modified.
    app.run(debug=True)
    # app.run(port=5000)
