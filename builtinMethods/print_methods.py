my_name = 'vincent'
my_age = '22'
print (my_name , my_age )
print('my name is ' +  my_name + 'my age' + my_age *2 )
print( f'my name is {my_name} my age is {my_age} ' )
print ('my name is {} my age is {}'.format(my_name, my_age) )
my_name = 'jimbazz'
my_age = '20'
my_state = 'Anambra'
my_hobby = 'games and reading'
my_color = 'black'
print (f'my name is {my_name} my age is {my_age} my state is {my_state} my hobby is {my_hobby} my color is {my_color}')
print ('my name is {} my age is {} my state is {} my hobby is {} my color is {}'. format (my_name , my_age , my_state, my_hobby,my_color))
def add_two_numbers (number_one, number_two) :
    return number_one + number_two
print (add_two_numbers(3,3))
def subtract_three_numbers (number_one, number_two, number_three) :
    return number_one - number_two - number_three
print (subtract_three_numbers (40,15, 20))
def multiply_three_numbers (number_one, number_two, number_three) :
    return number_one * number_two * number_three
print (multiply_three_numbers (40,15, 20))


def number_to_the_power_of_default(number_one, number_two=2):
    """Raise a number to an abitiary

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.
    """

    return number_one ** number_two

print (number_to_the_power_of_default(4))

def home():
    print("love football")
    print("love the game")
home()

marks = [23, 22, 34, 45,67,]
length = len(marks)
print ("length is", length)
marks_sum = sum (marks)
print ("total marks is ", marks_sum )



















