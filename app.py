from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)

@app.route('/post-endpoint', methods=['POST'])
def handle_post():
    data = request.get_json()
    response = {'received_data': data}
    return jsonify(response), 200

def run_flask():
    app.run(port=5000)

if __name__ == "__main__":
    thread = Thread(target=run_flask)
    thread.start()
