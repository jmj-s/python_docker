from flask import Flask, jsonify, request
from db import db
from Product import Product



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/products'
db.init_app(app)

# GET Products
# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    products = [product.json for product in Product.find_all()]
    return jsonify(products)

# GET Product

# curl -v http://localhost:5000/product/1
@app.route('/product/<int:id>')
def get_product(id):
    product = Product.find_by_id(id)
    if product:
        return jsonify(product.json)
    return f'Product not found', 404

# POST 

@app.route('/product', methods=['POST'])
def add_product():
    # Retrieve product from the request
    request_product = request.json

    product = Product(None, request_product['name'])

    product.save_to_db()

    return jsonify(product), 201


# PUT

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):

    existing_product = Product.find_by_id(id)

    if existing_product:
        # get request paylod
        updated_product = request.json

        existing_product.name = updated_product['name']
        existing_product.save_to_db()

        return jsonify(existing_product.json), 201
    
    return f'Product not found', 404




# DELETE

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    
    existing_product = Product.find_by_id(id)

    if existing_product:

        existing_product.delete_from_db()

        return f'Product successfully deleted', 200
    
    return f'Product with id {id} not found', 404



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
else:
    print("error")