from faker import Faker

fk_data = Faker('es_ES')
simpprof = fk_data.simple_profile()
print(simpprof)


curren = fk_data.currency()
print(curren)

curren = fk_data.currency_code()
print(curren)
