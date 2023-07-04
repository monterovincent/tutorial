# hello =lambda name : print(f'hello {name}')
# hello('john doe')
#
#
#
# sumnum = lambda fn, sn : fn + sn
# res = sumnum(7,3)
# print(res)





sum_num = lambda a : a + 5
res = sum_num(4)
print(sum_num)
print(res)



info = lambda  age, name: f'my name is {name} and my age is {age}'
my_info = info(12 , 'kola')
print(my_info)






val = lambda num: print('even number') if num%2== 0 else print('odd num')
val(43)





val = lambda num: print(f'even-----{num +num+0.05}') if num%2== 0 else print(f'{num-0.05-0.05}')


val(41)

#LAMBDA IN A FUNCTION
def mult(num):
    return lambda a: a*num
lam_val = mult(2)
lam_res = lam_val(4)
print(lam_res)








































