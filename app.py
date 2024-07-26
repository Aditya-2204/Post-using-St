from flask import Flask, request, jsonify
from threading import Thread
from pyngrok import ngrok
import time

app = Flask(__name__)

@app.route('/post-endpoint', methods=['POST'])
def handle_post():
    data = request.get_json()
    response = {'received_data': data}
    return jsonify(response), 200

def run_flask():
    app.run(port=5000)

def start_ngrok():
    # Open an ngrok tunnel to the local Flask server
    public_url = ngrok.connect(port='5000')
    print(f"Flask app is accessible at {public_url}")
    return public_url

if __name__ == "__main__":
    # Start ngrok tunnel
    start_ngrok()

    # Start Flask app in a separate thread
    thread = Thread(target=run_flask)
    thread.start()

    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        ngrok.disconnect()  # Disconnect ngrok when exiting
        ngrok.kill()         # Kill ngrok process
