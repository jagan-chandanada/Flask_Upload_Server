import base64
import flask
from flask import Flask, jsonify, make_response
import os, os.path

app = Flask(__name__)
counter = 1

@app.route('/upload', methods=['POST'])
def upload_picture():
    global counter
    b64_encodedImg = flask.request.form['image_string']
    image_category = flask.request.form['image_category']
    img_data = base64.b64decode(b64_encodedImg)
    image_filename = 'image' + str(counter) + '.jpg'
    counter += 1
    with open_safe_path(image_category + "/" + image_filename) as f:
        f.write(img_data)
    f.close()
    data = {'message': 'Done', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)

def open_safe_path(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'wb')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5100, debug=True)
