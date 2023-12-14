import json
from flask import Flask, Response

app = Flask(__name__)

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1472',
    autocommit=True
)

@app.route('/exercise_13-2/get_airport/<airport>')
def get_airport(airport):
    try:
        sql = 'SELECT ident, municipality, name FROM airport WHERE ident = %s;'

        cursor = connection.cursor()
        cursor.execute(sql, (airport,))
        result = cursor.fetchone()

        if result:
            icao, municipality, name = result
            response = {"ICAO": icao, "Name": name, "Location": municipality}
            return response
        else:
            response = {
                "message": "Airport not found",
                "status": 404
            }
            json_response = json.dumps(response)
            return Response(response=json_response, status=404, mimetype="application/json")

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=400, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
