import requests 
#set variable to product service 

#Cart Service--2nd microservice
def get_all_products():
    response = requests.get('http://127.0.0.1:5000/products')
    data = response.json()
    return data

#Endpoints htat interact with Produce Service 
if __name__ == '__main__':
    all_products = get_all_products()
    print("All Tasks:")
    print(all_products)

# /cart/{user id} (GET): Retrieve the current contents of a user’s shopping cart, including prod-
# uct names, quantities, and total prices.
# @app.route('/cart/<int: user_id>', methods=['GET'])
# def get_cart(product_id):
#     cart = next((task for task in tasks if task["id"] == task_id), None)
#     if task:
#         return jsonify({"task": task})
#     else:
#         return jsonify({"error": "Task not found"}), 404
# /cart/{user id}/add/{product id} (POST): Add a specified quantity of a product to the user’s cart.
# @app.route('/cart/<int: user_id>/add/<int: product_id>', methods=['POST'])
# def add_product(product_id):
# /cart/{user id}/remove/{product id} (POST): Remove a specified quantity of a product from the
# user’s cart
