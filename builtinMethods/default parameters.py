#default parameter for area of a circle



def area_circle( radius,pi = 3.142,  ):
    area = pi * (radius ** 2)
    return area

print(area_circle(5))


#FUNCTION CLASSWORK FOR SIMPLE ARITHEMETICS

def memo():
    print('welcome to our app')
    print('press 1 for addition')
    print('press 1 for subtraction')
    print('press 1 for multiplication')
    print('press 1 for divison')


def add_num(fn, sn):
    fn = int(input('enter first number'))
    sn = int(input('enter second number'))
    print(f'the result of {fn} + {sn} is {fn + sn}')



def sub_num(fn, sn):
    fn = int(input('enter first number'))
    sn = int(input('enter second number'))
    print(f'the result of {fn} - {sn} is {fn - sn}')


def multi_num(fn, sn):
    fn = int(input('enter first number'))
    sn = int(input('enter second number'))
    print(f'the result of {fn} * {sn} is {fn * sn}')


def div_num(fn, sn):
    fn = int(input('enter first number'))
    sn = int(input('enter second number'))
    print(f'the result of {fn} / {sn} is {fn / sn}')


def childapp():
    memo()
    option = input('please enter number between 1 and 4')

    if option == '1':
        add_num()
    elif option == '2':
        sub_num()

    elif option == '3':
        multi_num()


    elif option == '4':
        div_num()



print(childapp())

























































