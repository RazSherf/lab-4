from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (assuming it runs on the default container and port)
client = MongoClient("mongodb://mongo:27017/")
db = client['product_db']
products_collection = db['products']

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    product = {
        "name": data["name"],
        "price": data["price"],
        "amount": data["amount"]
    }
    result = products_collection.insert_one(product)
    return jsonify({"message": "Product added successfully", "id": str(result.inserted_id)})

@app.route('/get_products', methods=['GET'])
def get_products():
    products = list(products_collection.find({}, {"_id": 0}))  # Exclude _id from the result
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
