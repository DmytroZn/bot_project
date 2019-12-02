# from flask import Flask, request, Response
# from models.workers import Person
# from schemes.workers_schema import PersonSchema
# from flask_restful import Api
# from resources.worker_resourses import WorkerResource
# app = Flask(__name__)
# api = Api(app)

# api.add_resource(WorkerResource, '/workers', '/<string:id>')
# # app = Flask(__name__)


# # @app.route('/', methods = ['GET', 'POST'])
# # def hello_world():
# #     if request.method == 'GET':
# #         obj = Person.objects.get()
# #         return PersonSchema().dump(obj)
# #     else:
# #         validity =PersonSchema().validate(request.json)
# #         if validity:
# #             return validity
# #         Person(**request.json).save()
# #         return Response(status=201)



# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, Response
# from models.workers import Person
# from schemes.workers_schema import PersonSchema
from flask_restful import Api
from resources.product_resources import ProductResource
app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/product', '/product/<string:id>')





# @app.route('/', methods = ['GET', 'POST'])
# def hello_world():
#     if request.method == 'GET':
#         obj = Person.objects.get()
#         return PersonSchema().dump(obj)
#     else:
#         validity = PersonSchema().validate(request.json)
#         print(validity)
#         if validity:
#             return validity
#         Person(**request.json).save()
#         return Response(status=201)



if __name__ == '__main__':
    app.run(port=5001, debug=True)