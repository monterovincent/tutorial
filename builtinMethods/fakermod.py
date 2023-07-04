from faker import Faker

fk = Faker()
fk_name = fk.name()
print(fk_name)

fk_address = fk.address()
print(fk_address)

fk_firstname = fk.first_name()
print(fk_firstname)

fk_lastname = fk.last_name()
print(fk_lastname)



fk_data = Faker()
for _ in range(10):
    fn = fk_data.first_name()
    sn = fk_data.lastname()
    print(f'{fn}----{sn}')









