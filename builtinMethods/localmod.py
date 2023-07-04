from faker import Faker

fk_data = Faker('es_Es')
for _ in range(10):
    fn = fk_data.first_name()
    sn = fk_data.last_name()
    ph = fk_data.phone_number()
    jb = fk_data.job()
    print(f'{fn} {sn} {ph} {jb}')

