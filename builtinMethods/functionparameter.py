#FUNCTIONS PARAMETERS


# def say_hello(name):
#     return f'hello {name}'
#
# hello_res = say_hello('karim')
# print(hello_res)




#ATM WITHDRAWAL STRUCTURE

# balance = 0.00
# def save(amount):
#     global balance
#     balance = balance + amount
#     print (f'you have saved {balance}')
#
# save(20000)
#
#
# def withdraw(amount):
#     global balance
#     balance = balance - amount
#     return balance
#
#
# my_bal = withdraw(1000000)
# print(my_bal)


#function parameters for simple mathematics


def s_name(name,fn,sn):
    print(f' welcome {name}')
    res = fn + sn
    return f' {name}! the result of {fn} + {sn} is {res}'


res = s_name('john',4, 5)
print(res)




































