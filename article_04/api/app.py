from flask import Flask, jsonify, request, render_template
from faker import Faker
import os

fake = Faker()
app = Flask(__name__)

@app.route('/')
def index():
    pod_name = os.environ.get('HOSTNAME')
    return render_template('index.html', page_title = 'Home', pod_name = pod_name)

@app.route('/names', methods = ['GET'])
def get_name():
    if (request.method == 'GET'):
        pod_name = os.environ.get('HOSTNAME')
        new_name = fake.name()
        response = {'pod': pod_name, 'data': new_name}
        return jsonify(response)

@app.route('/license-plates', methods = ['GET'])
def get_license_plate():
    if(request.method == 'GET'):
        pod_name = os.environ.get('HOSTNAME')
        new_license_plate = fake.license_plate()
        response = {'pod': pod_name, 'data': new_license_plate}
        return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')