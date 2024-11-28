from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for orders
orders = []

# Endpoint to create a new order
@app.route('/create_order', methods=['POST'])
def create_order():
    # Extract the data from the request
    data = request.get_json()

    # Get the product name and quantity from the request
    product_name = data.get('product_name')
    quantity = data.get('quantity')

    if not product_name or not quantity:
        return jsonify({"error": "Product name and quantity are required"}), 400

    # Add the order to the orders list
    order = {"product_name": product_name, "quantity": quantity}
    orders.append(order)

    return jsonify({"message": "Order created successfully", "order": order}), 201

# Endpoint to get all orders
@app.route('/get_orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
