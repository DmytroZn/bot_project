from flask_restful import Resource
from flask import request, jsonify
from models.models import Product
from schemes.product_schema import ProductSchema

class ProductResource(Resource):



    def get(self, id=None):
        if not id:
            objects = Product.objects
            return ProductSchema().dump(objects, many=True)

        # return ProductSchema().dump(Product.objects(id=id).get())
        return jsonify(**{'method': 'get'})
        

        # return jsonify(**{'method': 'get'})


    
    def post(self):
        return jsonify(**{'method': 'post'})


    
    def put(self, id):
        obj = Product.objects(id=id).get()
        obj.update(**request.json)
        return ProductSchema().dump(obj.reload())
        # return jsonify(**{'method': 'put'})


    
    def delete(self):
        return jsonify(**{'method': 'delete'})