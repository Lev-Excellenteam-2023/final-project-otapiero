"""
This file is used to receive requests with files from the clients.
it has two endpoints:
 Upload : to receive a pptx file from the client.
 Status : to check the status of the explanation process.
"""
from flask import Flask, request, jsonify

from wep_api import uuid_handler, logic

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    """
    Receive a pptx file from the client.
    :return: json response with uuid of the file.
    """
    try:
        file = request.files['file']
        original_filename = file.filename
        user_id = uuid_handler.generate_uid()
        logic.create_file(user_id, original_filename, file.read())
        response = {'uid': user_id}
    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response)


@app.route('/status', methods=['GET'])
def status():
    """
    Check the status of the explanation process.
    :return: json response with the status.
    """
    pass

