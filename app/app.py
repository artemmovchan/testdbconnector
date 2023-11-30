from flask import Flask, request, jsonify
from services import send_sql_query_service


app = Flask(__name__)


@app.route("/health", methods=['GET', 'POST'])
def health():
    return jsonify(
        status = 'UP'
    )

@app.route("/call_function", methods=['POST'])
def call_function():
    try:
        data = request.get_json()
        result = send_sql_query_service(data)
        response = {
            'message': 'Success',
            'result': result
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'message': str(e)
        }
        return jsonify(response), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)