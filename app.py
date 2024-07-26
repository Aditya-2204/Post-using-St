from flask import Flask, request, jsonify
import streamlit as st

st.title("POST SERVER")

app = Flask(__name__)

@app.route('/post-endpoint', methods=['POST'])
def handle_post():
    # Get JSON data from the request
    data = request.get_json()

    # Process the data (for example, just echoing it back)
    response = {
        'received_data': data
    }

    # Send a JSON response
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

