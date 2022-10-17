from flask import Flask, jsonify, request

#esta app para el Flask para que el contenido este en la terminal antes señalizado
app = Flask(__name__)

#Aqui se importa la carpeta con algunos productos como ejemplo
from products import products

#Este pedazo es para observar si el LOCALHOST esta conectado
@app.route('/ping')
def ping():
    return jsonify({"mesasge": "pong!"})

@app.route('/products')
def getproducts():
    return jsonify({"products": products, "message": "Products's List"})

#Aqui se pueden ver los productos uno por uno si es necesario
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "product not found"})

#Este es para agregar algun producto con el nombre, precio y la cantidad 
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "products Added Succesfully", "products": products})

#Este es para modificar un solo campo de algun producto 
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProducts(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Update",
            "product": productsFound[0]
        })
    return jsonify({"message": "Product Not found"})

#Este es para eliminar un producto por completo
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteproduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len (productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message" : "Product Not Found"})

#Aqui se señaliza para el apartado en algun LOCALHOST
if __name__ == '__main__':
    app.run(debug = True, port = 4000)