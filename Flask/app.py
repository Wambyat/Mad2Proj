from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from celerySQL import cSQL
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
    output = cSQL.delay(query)
    while True:
        if output.status == "SUCCESS":
            return output.get()
        else:
            time.sleep(0.5)


# This is just a testing route. Use this to run sanity tests and whatever else.
@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify({"message": "This is a test message. From Flask."})


@app.route("/test/", methods=["GET", "POST"])
@jwt_required()
def test():
    global access_token
    return jsonify(
        {
            "access_token": access_token,
            "message": "You have sent it correctly!",
        }
    )


@app.route("/venue/", methods=["GET"])
def venue():
    res = SQL("SELECT * FROM venue")
    return jsonify({"data": res})


@app.route("/show/", methods=["GET"])
def show():
    res = SQL("SELECT * FROM show")
    return jsonify({"data": res})


@app.route("/show/<id>", methods=["GET"])
def show_id(id):
    res = SQL("SELECT * FROM show WHERE id = " + id)
    return jsonify({"data": res})


@app.route("/venue/<id>", methods=["GET"])
def venue_id(id):
    res = SQL("SELECT * FROM venue WHERE id = " + id)
    return jsonify({"data": res})


@app.route("/show/edit/<id>", methods=["POST"])
def show_edit(id):
    res = request.json
    name = res["name"]
    date = res["date"]
    venue = res["venue_id"]
    seats = res["seats"]
    details = res["details"]
    sql_query = (
        "UPDATE show SET name = '"
        + name
        + "', show_date = '"
        + date
        + "', venue_id = '"
        + venue
        + "', seats = '"
        + seats
        + "', details = '"
        + details
        + "' WHERE id = "
        + id
    )
    res = SQL(sql_query)
    return jsonify({"data": "res"})


@app.route("/venue/edit/<id>", methods=["POST"])
def venue_edit(id):
    res = request.json
    name = res["name"]
    address = res["address"]
    style = res["style"]
    sql_query = (
        "UPDATE venue SET name = '"
        + name
        + "', address = '"
        + address
        + "', style = '"
        + style
        + "' WHERE id = "
        + id
    )
    res = SQL(sql_query)
    return jsonify({"data": "res"})


@app.route("/show/add", methods=["POST"])
def show_add():
    res = request.json
    name = res["name"]
    date = res["date"]
    venue = res["venue_id"]
    seats = res["seats"]
    details = res["details"]
    sql_query = (
        "INSERT INTO show (name, show_date, venue_id, seats, details) VALUES ('"
        + name
        + "', '"
        + date
        + "', '"
        + venue
        + "', '"
        + seats
        + "', '"
        + details
        + "')"
    )
    res = SQL(sql_query)
    return jsonify({"data": "res"})


@app.route("/venue/add", methods=["POST"])
def venue_add():
    res = request.json
    name = res["name"]
    address = res["address"]
    style = res["style"]
    sql_query = (
        "INSERT INTO venue (name, address, style) VALUES ('"
        + name
        + "', '"
        + address
        + "', '"
        + style
        + "')"
    )
    res = SQL(sql_query)
    return jsonify({"data": "res"})


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
