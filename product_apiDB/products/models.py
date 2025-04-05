# from mongoengine import Document, StringField, FloatField

# class Product(Document):
#     name = StringField(required=True, max_length=200)
#     description = StringField()
#     price = FloatField(required=True)

#     meta = {'collection': 'products'}  # This ensures the correct collection name in MongoDB

from mongoengine import Document, StringField, FloatField, ReferenceField, ListField

class Product(Document):
    name = StringField(required=True)
    description = StringField()
    price = FloatField(required=True)
    brand = StringField(required=True)  # Required brand
    category = ReferenceField('ProductCategory', required=False)  # String reference to avoid circular import

class ProductCategory(Document):
    title = StringField(required=True, unique=True)
    description = StringField()
    products = ListField(ReferenceField('Product'))  # String reference to avoid circular import
