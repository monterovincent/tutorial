from prettytable import PrettyTable

ds = PrettyTable()
ds.field_names = ['country name','population','capital','currency']
ds.add_row(['Nigeria', 23000000,'Abuja', 'Naira'])
ds.add_row(['Ghana', 23000000,'Abuja', 'Naira'])
ds.add_row(['Togo', 23000000,'Abuja', 'Naira'])
ds.add_row(['Austria', 23000000,'Abuja', 'Naira'])

print(ds)


column_names = ['Nigeria data','Ghana data','Togo data','Austria data']
dt.add_column(column_names[0], ['Nigeria',230000,'Abuja','Naira'])
dt.add_column(column_names[1], ['Ghana',230000,'Abuja','Naira'])
dt.add_column(column_names[2], ['Togo',230000,'Abuja','Naira'])
dt.add_column(column_names[3], ['Austria',230000,'Abuja','Naira'])

print(dt)


