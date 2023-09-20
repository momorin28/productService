from flask import Flask, jsonify, request
app = Flask(__name__)

# names prices and quanitity 
products = [
    {"id": 1, "name": "chocolate", "price": 5, "quantity": 1},
    {"id": 2, "name": "gum", "price": 2.5, "quantity": 2},
    {"id": 3, "name": "chips", "price": 3, "quantity": 2}
]

# Endpoint 1: /products (GET): Retrieve a list of available grocery products, including their names, prices, and
# quantities in stock.
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})

# #endpoints --

# /products/product id (GET): Get details about a specific product by its unique ID.
# Endpoint 2: Get a specific task by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

# /products (POST): Allow the addition of new grocery products to the inventory with information
# such as name, price, and quantity
@app.route('/products', methods=['POST'])
def create_products():
    new_product = {
        "id": len(products) + 1,
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "quantity": request.json.get('quantity')
    }
    products.append(new_product)
    return jsonify({"message": "Product created", "product": new_product}), 201


#last endpoint, will have additional json --allow for addition and subtraction 
if __name__ == '__main__':
    app.run(debug=True)
