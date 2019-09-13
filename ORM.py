# Работа с БД
from peewee import SqliteDatabase, Model, CharField, DateField, BooleanField, ForeignKeyField
from datetime import date

db = SqliteDatabase('people1.db')

class Person(Model):
    name = CharField()
    data_of_birth = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


Person.create_table()
uncle_bob = Person(name="Bob", data_of_birth=date(1999,1,1), is_relative=True)
uncle_bob.save()
Person.create(name="Jim", data_of_birth=date(1907,1,1), is_relative=True)

bobs = list(Person.select().where(Person.name == "Bob"))
# bobs
# print(bobs[1].data_of_birth)
bob = bobs[0]
# bob.name = "Bobby"
# bob.is_relative = True
# bob.save()


class Pet(Model):
    name = CharField()
    animal_type = CharField()
    owner = ForeignKeyField(Person, related_name="pets")

    class Meta:
        database = db

Pet.create_table()

Pet.create(name="Lucy", animal_type="cat", owner=bob)