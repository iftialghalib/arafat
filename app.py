from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(_name_)
api = Api(app)

# Contoh data produk
products = {
    "1": {"name": "Product 1", "price": 100},
    "2": {"name": "Product 2", "price": 200},
    "3": {"name": "Product 3", "price": 300}
}

class ProductList(Resource):
    def get(self):
        return jsonify(products)

class ProductDetail(Resource):
    def get(self, product_id):
        product = products.get(product_id)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        new_id = str(len(products) + 1)
        data = request.get_json()
        products[new_id] = data
        return {"message": "Product added", "product": products[new_id]}, 201

class UpdateProduct(Resource):
    def put(self, product_id):
        if product_id in products:
            data = request.get_json()
            products[product_id].update(data)
            return {"message": "Product updated", "product": products[product_id]}
        return {"message": "Product not found"}, 404

class DeleteProduct(Resource):
    def delete(self, product_id):
        if product_id in products:
            deleted_product = products.pop(product_id)
            return {"message": "Product deleted", "product": deleted_product}
        return {"message": "Product not found"}, 404

# Menambahkan endpoint ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<string:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<string:product_id>')

if _name_ == '_main_':
    app.run(debug=True)
