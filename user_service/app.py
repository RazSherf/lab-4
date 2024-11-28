from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')  # mongo is the service name in docker-compose
db = client['user_db']  # Database name
users_collection = db['users']  # Collection name

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    user = {
        "username": username,
        "email": email
    }

    result = users_collection.insert_one(user)
    return jsonify({"message": "User added", "user_id": str(result.inserted_id)}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
