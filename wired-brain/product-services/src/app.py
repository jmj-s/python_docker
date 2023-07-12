from flask import Flask, jsonify, request

products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'},
]

app = Flask(__name__)

# GET Products
# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(products)

# GET Product

# curl -v http://localhost:5000/product/1
@app.route('/product/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 0:
        return f'Product with id {id} not found', 404
    return jsonify(product_list[0])

# POST 

@app.route('/product', methods=['POST'])
def add_product():
    # Retrieve product from the request
    request_product = request.json

    # Generate an ID for the post
    new_id = max([product['id'] for product in products]) + 1

    # Create a new product
    new_product = {
        'id': new_id,
        'name': request_product['name']
    }

    # Append the new product to our product list
    products.append(new_product)

    return jsonify(new_product), 201

# PUT

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    
    updated_product = request.json

    for product in products:
        if product['id'] == id:
            product['name'] = updated_product['name']
            return jsonify(product), 200
    
    return f'Product with id {id} not found', 404

# DELETE

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 1:
        products.remove(product_list[0])
        return f'Product with id {id} successfully deleted', 200
    
    return f'Product with id {id} not found', 404



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
else:
    print("error")