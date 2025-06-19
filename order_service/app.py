from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# Initialize Prometheus metrics with automatic HTTP request monitoring
metrics = PrometheusMetrics(app)

# Add a default metrics endpoint at /metrics
# This will automatically track HTTP request counts, durations, and status codes
metrics.info('app_info', 'Order service application information', version='1.0.0')

# In-memory storage for orders
orders = []

# Health check endpoint - required for Kubernetes probes
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status1": "healthy"}), 200

# Endpoint to create a new order
@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    product_name = data.get('product_name')
    quantity = data.get('quantity')

    if not product_name or not quantity:
        return jsonify({"error": "Product name and quantity are required"}), 400

    order = {"product_name": product_name, "quantity": quantity}
    orders.append(order)

    return jsonify({"message": "Order created successfully", "order": order}), 201

# Endpoint to get all orders
@app.route('/get_orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)