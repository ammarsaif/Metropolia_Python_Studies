import json

from flask import Flask, Response

app = Flask(__name__)


def is_prime(number):
    try:
        num = int(number)
        if num <= 1:
            return f"{num} is not a prime number"
        elif num == 2:
            return f"{num} is a prime number"
        else:
            for i in range(2, num):
                if num % i == 0:
                    return f"{num} is not a prime number"
            return f"{num} is a prime number"

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=400, mimetype="application/json")


@app.route('/exercise_13/prime_number/<number>')
def prime_number(number):
    is_prime_result = is_prime(number)
    response = {
        "num": number,
        "result": is_prime_result
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200, mimetype="application/json")
    return http_response


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
