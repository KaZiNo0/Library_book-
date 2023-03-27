from peewee import *


class LibraryModel(Model):
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100)
    year = IntegerField()
    author = CharField(max_length=100)
    count_pages = IntegerField()

    class Meta:
        db_table = "book"
        order_by = ("id",)
