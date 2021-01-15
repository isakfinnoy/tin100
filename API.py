
from database import open_database
import flask
from flask import request, jsonify, abort
import sqlite3


import time
from datetime import datetime

app = flask.Flask(__name__)


@app.route('/insert', methods=["POST"])
def insert():
    """Endepunkt for å motta data fra en sensor
    """

    with sqlite3.connect('database.db') as con:
        # Slipper å lukke databasen manuelt med denne syntaksen
        c = con.cursor()
        value = request.args["value"] # Henter value fra argumentene
        date = time.time() # Henter tiden nå

        print(datetime.fromtimestamp(date)) # Printer ut tiden på et litt finere format

        # Setter inn i sensordata-tabellen value og tiden nå
        sql_insert = f'INSERT INTO sensordata (value, date) VALUES ({value}, {date})'
        print(sql_insert)
        c.execute(sql_insert)

        con.commit()

    return "suksess"


@app.route('/get_all', methods=["GET"])
def get_all():
    """Endepunkt for å hente all data ut fra databasen 
    """
    with sqlite3.connect('database.db') as con:
        c = con.cursor()
        sql_get = f'SELECT * from sensordata'

        c.execute(sql_get)

        rows = c.fetchall()

        print(rows)

        return jsonify(rows)


@app.route('/get_value', methods=["GET"])
def get_value():
    """Endepunkt for å hente et datapunkt basert på id i databasen 
    """
    with sqlite3.connect('database.db') as con:

        id = request.args["id"]

        c = con.cursor()

        # Henter ut value og date basert på id i databasen
        sql_get = f'SELECT value, date FROM sensordata WHERE id={id}'

        c.execute(sql_get)

        rows = c.fetchone()

        if rows == None:
            print(rows)
            abort(404, "") # Gir en 404 (Ikke funnet) hvis ingen rader ble funnet i databasen med oppgitt id
        else:
            return jsonify(rows)


app.run(debug=True)
