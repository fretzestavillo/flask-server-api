from flask import Flask, request, jsonify
from pymongo import MongoClient, errors
from flask_cors import CORS

# my flask server http://127.0.0.1:5000
# my mongodb server localhost:27017

app = Flask(__name__)
CORS(app)
# Connect to MongoDB
try:
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sample_db']  # Replace with your database name
    collection = db['sample_collection']  # Replace with your collection name
    print("Connection to MongoDB successful.")
except errors.ConnectionError as conn_err:
    print(f"Connection error: {conn_err}")
except errors.ConfigurationError as config_err:
    print(f"Configuration error: {config_err}")
except errors.OperationFailure as op_err:
    print(f"Operation failure: {op_err}")
except Exception as e:
    print(f"An error occurred: {e}")


# Sample data for insertion
# sample_data = [
#     {"name": "John Doe", "age": 30, "city": "New York"},
#     {"name": "Jane Smith", "age": 25, "city": "San Francisco"},
#     {"name": "Tom Brown", "age": 35, "city": "Chicago"}
# ]

# Insert sample data into MongoDB collection
# for data in sample_data:
#     collection.insert_one(data)

@app.route('/')
def index():
    return "This is an API bitch"



# get all data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = []
    for doc in collection.find():
        data.append({
            'name': doc['name'],
            'age': doc['age'],
            'city': doc['city']
        })
    return jsonify(data), 200

# get property and all of its key/value
@app.route('/api/data/<name>', methods=['GET'])
def get_data_by_name(name):
    doc = collection.find_one({'name': name})
    if doc:
        return jsonify({
            'name': doc['name'],
            'age': doc['age'],
            'city': doc['city']
        }), 200
    else:
        return jsonify({'error': 'Name not found'}), 404
    


# I dont know the below on how it works!

# @app.route('/api/data', methods=['POST'])
# def add_data():
#     new_data = request.get_json()
#     if isinstance(new_data, dict):  # Ensure data is a dictionary
#         collection.insert_one(new_data)
#         return jsonify({'message': 'Data added successfully'}), 201
#     else:
#         return jsonify({'error': 'Invalid JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
