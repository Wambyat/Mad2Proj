from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from celerySQL import cSQL, cemail
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


def email(query, sub, bod):
    output = cemail.delay(query, sub, bod)
    while True:
        if output.status == "SUCCESS":
            return output.get()
        else:
            time.sleep(0.5)


# This is just a testing route. Use this to run sanity tests and whatever else.
@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify({"message": "This is a test message. From Flask."})


@app.route("/alerts/", methods=["GET"])
def alerts():
    res = SQL(
        "SELECT email FROM user_details WHERE id in (SELECT user_id FROM ticket WHERE date_booked < DATE('now','-1 month') AND user_id NOT IN (SELECT id FROM admin) AND user_id NOT IN (SELECT user_id FROM ticket WHERE date_booked > DATE('now','-1 month')))"
    )
    print("RESULT:ASFDKBJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJJjn\n\n\n\n\n"+str(res))
    for i in res:
        email(
            i[0],
            "Alert",
            "You have not booked a ticket in the last month. Please book a ticket soon.",
        )
    return jsonify({"data": "res"})

@app.route("/report/", methods=["GET"])
@jwt_required()
def report():
    id = get_jwt_identity()
    res = SQL("SELECT t.id, s.name, s.show_date, s.seats_booked FROM ticket t join show s WHERE date_booked > DATE('now','-1 month') AND t.show_id = s.id AND user_id = "+str(id))
    if len(res) == 0:
        return jsonify({"data": "No tickets booked"})
    else:
        return jsonify({"data": res})

@app.route("/test/", methods=["GET", "POST"])
@jwt_required()
def test():
    global access_token
    user_id = get_jwt_identity()
    return jsonify(
        {
            "access_token": access_token,
            "user_id": user_id,
            "message": "You have sent it correctly!",
        }
    )


@app.route("/user/", methods=["POST", "GET"])
@jwt_required()
def user():
    global access_token
    # get jwt identity
    user_id = get_jwt_identity()
    if request.method == "POST":
        res = request.json
        username = res["username"]
        password = res["password"]
        fname = res["fname"]
        lname = res["lname"]
        age = res["age"]
        email = res["email"]
        res = SQL(
            "UPDATE users SET username = '"
            + username
            + "', password = '"
            + password
            + "' WHERE id = "
            + str(user_id)
        )

        # check if user details exist
        res = SQL("SELECT * FROM user_details WHERE id = " + str(user_id))
        if len(res) == 0:
            res = SQL(
                "INSERT INTO user_details VALUES ("
                + str(user_id)
                + ", '"
                + fname
                + "', '"
                + lname
                + "', "
                + str(age)
                + ", '"
                + email
                + "')"
            )
        else:
            res = SQL(
                "UPDATE user_details SET fname = '"
                + fname
                + "', lname = '"
                + lname
                + "', age = "
                + str(age)
                + ", email = '"
                + email
                + "' WHERE id = "
                + str(user_id)
            )
        return jsonify({"data": "res"})
    else:
        res = SQL(
            "SELECT u.id, u.username, u.password, ud.fname, ud.lname, ud.age, ud.email from users u join user_details ud on u.id = ud.id WHERE u.id = "
            + str(user_id)
        )
        return jsonify({"data": res})


@app.route("/ticket/", methods=["GET"])
@jwt_required()
def ticket():
    global access_token
    # get jwt identity
    user_id = get_jwt_identity()
    res = SQL(
        "SELECT a.id, v.name, a.seats, a.name, a.show_date, a.details, a.date_booked FROM (SELECT t.id, t.seats, t.date_booked, s.name, s.show_date, s.venue_id, s.details FROM ticket t join show s on t.show_id = s.id WHERE t.user_id = "
        + str(user_id)
        + ") a join venue v on a.venue_id = v.id"
    )
    return jsonify({"data": res})


@app.route("/ticket/<id>", methods=["GET", "POST"])
@jwt_required()
def ticket_id(id):
    global access_token
    # get jwt identity
    user_id = get_jwt_identity()
    tid = SQL("SELECT MAX(id) FROM ticket")[0][0] + 1
    tid = str(tid)
    reque = request.json
    seats = reque["seats"]
    res = SQL(
        "INSERT INTO ticket VALUES ("
        + tid
        + ", "
        + str(id)
        + ", "
        + str(user_id)
        + ", "
        + str(seats)
        + ", DATE('now'))"
    )
    # update seats booked and seats left in show
    res = SQL("SELECT seats_booked, seats FROM show WHERE id = " + str(id))
    seats_booked = res[0][0]
    seats_left = res[0][1]
    seats_booked += int(seats)
    seats_left -= int(seats)
    res = SQL(
        "UPDATE show SET seats_booked = "
        + str(seats_booked)
        + ", seats = "
        + str(seats_left)
        + " WHERE id = "
        + str(id)
    )
    return jsonify({"data": res})


@app.route("/show/", methods=["GET"])
def show():
    res = SQL("SELECT * FROM show")
    return jsonify({"data": res})


@app.route("/show/<id>", methods=["GET"])
def show_id(id):
    res = SQL("SELECT * FROM show WHERE id = " + id)
    return jsonify({"data": res})


@app.route("/show/tags/<id>", methods=["GET"])
def show_tags(id):
    res = SQL(
        "SELECT t.name FROM tag t join show_tags st on t.id = st.tag_id WHERE st.show_id = "
        + id
    )
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


@app.route("/show/add", methods=["POST"])
def show_add():
    res = request.json
    name = res["name"]
    date = res["date"]
    venue = res["venue_id"]
    seats = res["seats"]
    details = res["details"]
    id = SQL("SELECT MAX(id) FROM show")[0][0] + 1
    id = str(id)
    sql_query = (
        "INSERT INTO show (id, name, show_date, venue_id, seats, seats_booked, details) VALUES ("
        + id
        + ", '"
        + name
        + "', '"
        + date
        + "', '"
        + venue
        + "', '"
        + seats
        + "', "
        + "0, '"
        + details
        + "')"
    )
    res = SQL(sql_query)
    return jsonify({"data": "res"})


@app.route("/show/delete/<id>", methods=["GET"])
def show_delete(id):
    sql_query = "DELETE FROM show WHERE id = " + id
    res = SQL(sql_query)
    return jsonify({"data": "res"})


@app.route("/venue/", methods=["GET"])
def venue():
    res = SQL("SELECT * FROM venue")
    return jsonify({"data": res})


@app.route("/venue/<id>", methods=["GET"])
def venue_id(id):
    res = SQL("SELECT * FROM venue WHERE id = " + id)
    return jsonify({"data": res})


@app.route("/venue/add", methods=["POST"])
def venue_add():
    res = request.json
    name = res["name"]
    address = res["address"]
    style = res["style"]

    sql_query = (
        "INSERT INTO venue (id, name, address, style) VALUES ("
        + id
        + ", '"
        + name
        + "', '"
        + address
        + "', '"
        + style
        + "')"
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


@app.route("/venue/delete/<id>", methods=["GET"])
def venue_delete(id):
    sql_query = "DELETE FROM venue WHERE id = " + id
    res = SQL(sql_query)
    return jsonify({"data": "res"})


@app.route("/venue/export/<id>", methods=["GET"])
def venue_export(id):
    res = SQL(
        "SELECT t.id, t.seats FROM ticket t join (SELECT venue_id, id FROM show) vs WHERE t.show_id = vs.id AND vs.venue_id = "
        + id
    )
    res2 = SQL("SELECT id, show_date FROM show WHERE venue_id = " + id)
    return jsonify({"tickets": res, "shows": res2})


@app.route("/login", methods=["POST"])
def login():
    global access_token
    username = request.json.get("username")
    password = request.json.get("password")
    res = SQL("SELECT * FROM users")
    # print(res)
    us = [i[1] for i in res]
    if username not in us:
        id = SQL("SELECT MAX(id) FROM users")[0][0] + 1
        id = str(id)
        res = SQL("INSERT INTO users VALUES (" + id + ", '" + username + "', '" + password + "')")
        access_token = create_access_token(identity=id)
        return jsonify(
            {
                "access_token": access_token,
                "message": "You are logged in now",
                "admin": False,
            }
        )
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
