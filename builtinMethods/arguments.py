#ARGS (ARGUEMENTS)


# def myfood(*args):
#     return args
#
#
# food = myfood('noodles','rice','beans')
# print(food)





#KWARGS KEYWORD DOCUMENTS

# def african_countries(**kwargs):
#     return kwargs
#
# country = african_countries(one='ghana',two='egypt',three='capetown')
# print(country)






# def epl_league(**kwargs):
#     return kwargs
#
# country = epl_league(one='mancity',two='westham',three='wolves')
# print(country)





def epl_league(**kwargs):
    for k,v in kwargs.items():
        return kwargs



res = epl_league(one='mancity',two='westham',three='wolves')
for k, v in res.items():
    print(f'{k}----{v}')

























