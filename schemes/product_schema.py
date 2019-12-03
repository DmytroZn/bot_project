from marshmallow import (
    fields, Schema, 
    validates, ValidationError
)
from models import *


# class LocationSchema(Schema):
#     city= fields.String()
#     street = fields.String()


# class PersonSchema(Schema):
#     id = fields.String()
#     first_name = fields.String()
#     surname = fields.String()
#     age = fields.Integer()
#     experience = fields.Integer()
#     location = fields.Nested(LocationSchema)


#     @validates('age')
#     def validate_age(self, value):
#         if value > 65:
#             raise ValidationError('The age must be less than 65')

class TextsSchema(Schema):
    title = fields.String(unique=True)
    body = fields.String(max_lenght=4096)


class PropertiesSchema(Schema): 
    weight = fields.Float()


class CategorySchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    subcategory = fields.List(fields.Nested('self'), load_only=True)
    # subcategory = ListField(ReferenceField('self'))
    # parent = ReferenceField('self')
    parent = fields.Nested('self')


class ProductSchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    price = fields.Integer()
    new_price = fields.Integer()
    is_discount = fields.Boolean()
    properties = fields.Nested(PropertiesSchema)
    # category = fields.Nested(models.Category.objects().get()) #load_only=True
    # photo = FileField()
    category = fields.Nested(CategorySchema)
    # category = fields.String()

    

# class ProductSchemaWrite(Schema):
#     id = fields.String()
#     title = fields.String()
#     description = fields.String()
#     price = fields.Integer()
#     new_price = fields.Integer()
#     is_discount = fields.Boolean()
#     properties = fields.Nested(PropertiesSchema)
#     # category = fields.Nested(models.Category.objects().get()) #load_only=True
#     # photo = FileField()
#     category = fields.Nested(models.Category.objects().get())




