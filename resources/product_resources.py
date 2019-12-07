from flask_restful import Resource
# from flask import request, jsonify
from models.models import * #, Product
from schemes.product_schema import *#, ProductSchema
from flask import Flask, request,jsonify, Response
from models import *


class ProductResource(Resource):

    def get(self, id=None):
        print('200 - 80')
        if not id:
            objects = Product.objects
            return ProductSchema().dump(objects, many=True)
        return ProductSchema().dump(Product.objects(id=id).get())
        # return jsonify(**{'method': 'get'})

    def post(self):
        validity = ProductSchema().validate(request.json)
        print(validity)
        if validity:
            return validity
        Product(**request.json).save()
        return Response(status=201)
        # return jsonify(**{'method': 'post'})
    
    def put(self, id):
        obj = Product.objects(id=id).get().delete()
        obj = Product(**request.json).save()
        # obj.update(**request.json)
 
        return ProductSchema().dump(obj)
        # return jsonify(**{'method': 'put'})



    # def put(self, id):
    #     obj = Product.objects(id=id).get()

    #     obj.update(**request.json)
 
    #     return ProductSchema().dump(obj.reload())
    #     # return jsonify(**{'method': 'put'})
  
    def delete(self, id):
        Product.objects(id=id).delete()
        # return jsonify(**{'method': 'delete'})




class CategoryResource(Resource):

    def get(self, id=None):
        if not id:
            objects = Category.objects
            return CategorySchema().dump(objects, many=True)
        return CategorySchema().dump(Category.objects(id=id).get())
        # return jsonify(**{'method': 'get'})

    def post(self):
        validity = CategorySchema().validate(request.json)
        print(validity)
        if validity:
            return validity
        Category(**request.json).save()
        return Response(status=201)
        # return jsonify(**{'method': 'post'})
    
    def put(self, id):
        obj = Category.objects(id=id).get()
        obj.update(**request.json)
        return CategorySchema().dump(obj.reload())
        # return jsonify(**{'method': 'put'})

    def put(self, id):
        obj = Category.objects(id=id).get()
        Category(**request.json).save()
        # obj.update(**request.json)
        # return CategorySchema().dump(obj.reload())
        # return jsonify(**{'method': 'put'})
  
    def delete(self, id):
        Category.objects(id=id).delete()
        # return jsonify(**{'method': 'delete'})