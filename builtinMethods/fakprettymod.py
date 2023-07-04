from faker import Faker
from prettytable import PrettyTable

fk = Faker()
pt = PrettyTable()

fk_firstname = fk.first_name()
fk_lastname = fk.last_name()
fk_jb = fk.job()
fk_em = fk.email()

pt.field_names = ['firstname','lastname','jobs','email']
pt.add_row([fk_firstname, fk_lastname,fk_jb, fk_em])
pt.add_row([fk_firstname, fk_lastname,fk_jb, fk_em])
pt.add_row([fk_firstname, fk_lastname,fk_jb, fk_em])
pt.add_row([fk_firstname, fk_lastname,fk_jb, fk_em])
pt.add_row([fk_firstname, fk_lastname,fk_jb, fk_em])
print(pt)











