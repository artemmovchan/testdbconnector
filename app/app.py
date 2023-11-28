from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/health", methods=['POST'])
def health():
    return jsonify(
        status = 'UP'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)