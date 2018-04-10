import peewee

database = peewee.SqliteDatabase('products.db')

class Products(peewee.Model):
    product_id = peewee.CharField(unique=True)
    product_name = peewee.CharField()
    product_image = peewee.CharField()

    class Meta:
        database = database

class Tags(peewee.Model):
    product_id = peewee.ForeignKeyField(Products, to_field="product_id")
    general_tag = peewee.CharField()
    logo_tag = peewee.CharField()
    color_tag = peewee.CharField()

    class Meta:
        database = database

