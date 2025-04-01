from mongoengine import Document, StringField, FloatField

class Product(Document):
    name = StringField(required=True, max_length=200)
    description = StringField()
    price = FloatField(required=True)

    meta = {'collection': 'products'}  # This ensures the correct collection name in MongoDB
