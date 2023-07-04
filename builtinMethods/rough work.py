#DICTIONARIES IN PYTHON
# import random

# capitals= {'USA':'washington',
#            'russia':'moscow',
#            'germany':'berlin',
#            'nigeria':'abuja'}
# print(capitals['nigeria'])
#
# print(capitals.get('germany'))


#INDEXING OPERATORS/STRINGS/TUPLES



# myname = 'code bro'
# # if(myname[3].islower()):
# #     myname= myname.capitalize()
# # print(myname)
#
#
#
#
# first_name = myname[0:4].upper()
# last_name = myname[4:].lower()
#
# print(first_name)
#
# print(last_name)





#FUNCTIONS IN PYTHON


# def hello(firstname,lastname,age):
#     print('hello'+ firstname +" "+ lastname)
#     print("you are"+str(age)+"years old")
#     print("have a nice day!")
#
#
# hello("bro","code",22)




#RETURN STATEMENTS IN PYTHON

# def multiply(num1,num2):
#     return num1 * num2
# x = multiply(6,2)
# print(x)
#
#
# #KEYWORD ARGUEMENTS
#
# def hello(first,last,middle):
#     print('hello > ' + first +  " " +middle +" " +last)
#
# hello("bro","dude","code")
#
#
# #NESTED FUNCTION CALLS
#
# # num =  input('enter a whole postive number :')
# # num =float(num)
# # num = abs(num)
# # num = round(num)
# # print(num)
#
#
# print(round(abs(float(input('enter a whole postive number :')))))
#
# #VARIABLE SCOPE


# name = 'bro'
#
# def display_name():
#     name = 'code'
#     print(name)
#
# display_name()
# print(name)


#ARC PARAMETERS IN PYTHON (ASTERIX ARGS)


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#         return sum
#
# print(add(1,2,3,4,5,6,))




#PESUDO RANDOM NUMBERS



x = random.randint(1,6)
y = random.random()
mylist = ['broom','glory','kareem','nokia']
z = random.choice(mylist)
cards = [1,2,3,4,5,6,7,8,'j','m','g','h','g']
random.shuffle(cards)

print(cards)























