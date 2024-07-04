from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'

# @app.route('/')
# def home():
#     return jsonify({'message': 'Welcome to the Flask API!'})

@app.route('/api/v1/resource', methods=['GET'])
def get_resource():
    return jsonify({'resource': 'This is a resource'})

@app.route('/api/v1/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    return jsonify({'resource': data}), 201

@app.route('/api/v1/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.get_json()
    return jsonify({'resource': f'Updated resource {id} with data {data}'}), 200

@app.route('/api/v1/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    return jsonify({'message': f'Resource {id} deleted'}), 200

