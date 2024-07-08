"""
This file is used to receive requests with files from the clients.
it has two endpoints:
 Upload : to receive a pptx file from the client.
 Status : to check the status of the explanation process.
"""
import logging

from flask import Flask, request, jsonify, abort

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
    except FileExistsError as e:
        response = {'error': str(e)}
    except OSError as e:
        print(e)
        response = {'error': "error while uploading the file."}
    return jsonify(response)


@app.route('/status', methods=['GET'])
def status():
    """
    Check the status of the explanation process.
    :return: json response with the status.
    """
    try:
        uid = request.args.get('uid')
        response = logic.create_response(uid)
        return jsonify(response)
    except FileNotFoundError as e:
        abort(404)
    except OSError as e:
        logging.error(e)
        print(e)
        abort(500)


if __name__ == '__main__':
    app.run()
#curl -X POST -F "file=@C:/Users/ouriel/Desktop/End of course exercise - kickof - upload.pptx" http://localhost:5000/upload
#curl -X GET http://localhost:5000/status?uid=0e8e2b2e-0b0b-4b0e-9b0a-0b0b0b0b0b0b