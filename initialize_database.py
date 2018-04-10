import peewee

database = peewee.SqliteDatabase('products.db')

class Products(peewee.Model):
    product_id = peewee.CharField(unique=True)
    product_name = peewee.CharField()
    product_image = peewee.CharField()

    class Meta:
        database = database

class Vendor_Availabilty(peewee.Model):
    product_id = peewee.ForeignKeyField(Products, to_field="product_id")
    vendor_id = peewee.IntegerField()
    vendor_name  = peewee.CharField()
    price = peewee.DoubleField()
    quantity = peewee.IntegerField()

    class Meta:
        database = database

class Tags(peewee.Model):
    product_id = peewee.ForeignKeyField(Products, to_field="product_id")
    general_tag = peewee.CharField()
    logo_tag = peewee.CharField()
    color_tag = peewee.CharField()

    class Meta:
        database = database

def initialize_db():
    database.create_tables([Products, Vendor_Availabilty, Tags], safe=True)

initialize_db()