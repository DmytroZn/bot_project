from marshmallow import (
    fields, Schema, 
    validates, ValidationError
)



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

class PropertiesSchema(Schema): # не важные характеристикаи , ссылка
    weight = fields.Float()

class ProductSchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    price = fields.Integer()
    new_price = fields.Integer()
    is_discount = fields.Boolean()
    properties = fields.Nested(PropertiesSchema)
    category = fields.String() #load_only=True
    # photo = FileField()
