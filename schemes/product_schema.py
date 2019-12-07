from marshmallow import (
    fields, Schema, 
    validates, ValidationError
)
from models import *

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
    category = fields.Nested(CategorySchema)





