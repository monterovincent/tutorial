from faker import Faker

fk_data = Faker()
for _ in range(10):
    fn = fk_data.first_name()
    sn = fk_data.last_name()
    print(f'{fn}----{sn}')







