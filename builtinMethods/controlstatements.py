# num = 10
# if num < 20 :
#     print(num)
#one way ifstatement

#two way if statement

# user_name = 'brain'
# pass_word = 'cream'
# if (user_name == 'brain') and (pass_word == 'cream') :
#     print ('welcome to dash board')
#
# else:
#     print('credentials are correct')



#multiIFstatement

# day = input ('please enter day of the week >>> ')
#
# if day == 'monday':
#     print ('go to work')
#
# elif day == 'tuesday' :
#     print ('go to church')
#
# else :
#     print ('please a day of the week')


#nestedIFstatement

# user_name = 'brain'
# pass_word = 'cream'
# if (user_name == 'brain') and (pass_word == 'cream') :
#      print ('welcome to dash board')
#
#
#
# else:
#     print('credentials are correct')



emp_name = input ('enter your name')
sales_over_year = float (input ('please enter sales over 5 years >>>> '))
year_in_comp = int (input ('please enter your year >>>>> '))
emp_sales = float (input('please enter your salary >>>> '))
if year_in_comp >= 5:
    if sales_over_year >= 20_000_000:
        sale_incre = emp_sales * 0.5
        new_sal = emp_sales + sale_incre
        print ( f'congrats!!!!! mr/mrs {emp_name} your previous {emp_sales}')
        f'salary has been increased by 50%'
        f' new salary is ne{new_sal}'





else:
    print (f'mr/mrs {emp_name}, you did not meet up with your sale this year'
               f' so your salary remains {emp_sales}')





























