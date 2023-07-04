from pydal import DAL, Field


db = DAL('sqlite://test.db',folder = 'db')
db.define_table('cars',Field('name'), Field('price',type = 'integer'))
db.cars.insert(name = 'Audi', price = 3445)
db.cars.insert(name = 'Honda', price = 222)
db.cars.insert(name = 'Toyota', price = 3456)
db.cars.insert(name = 'RangeRover', price = 678)
db.cars.insert(name = 'Bugatti', price = 2908)
db.cars.insert(name = 'Benz', price = 6753)
db.cars.insert(name = 'Lexus', price = 2908)
db.cars.insert(name = 'Bmw', price = 23498)
db.close()
