# ran_num = range(10)
# print(ran_num)
# ran_num2 = range(5,20 )
# print(ran_num2)
# for num in ran_num:
#     print(num)
#
# for num in ran_num2 :
#     print(num)

#range in sequence and iteriables
# nums = range (0,6)
# print(nums)
# for num in nums:
#     print(num)


# vals= range (7, 50,3)
# for val in vals :
#     print(val)



# vals= range (100, 100000)
# for val in vals:
#     print(val)
#
# startval = vals.start
# print(startval)
#
#
# stopval = vals.stop
# print(stopval)
#
#
#
# gene= range (-13 , 63)
# print(len(gene))


#STRING IN SEQUENCE AND ITERIABLES


# country = 'nigeria'
# ourpresident = "obi"
# ourstory = "we are always divided as a nation "
# print(country, ourpresident, ourstory)
# for c in country:
#     print(c)


#STRING SLICING

# greet = 'congratulations'
# print(len(greet))
# slice_one = greet[0:9:2]
# print(slice_one)


#STRINGS METHODS

# greet = 'CONGRATULATIONS'
# str_low = greet.lower()
# print(str_low)
#
#
# greet= 'CONGRATULATIONS'
# str_upper = greet.upper()
# print(str_upper)




#LIST IN SEQUENCE AND ITERIABLES

# anims = ['goat', 'cow', 'ram', 'sheep']
# anims[3] = 'elephant'
# print(anims[3])
# print(anims)
#
#
# my_students = list()
# my_students.append('brazil')
# my_students.append('mexico')
# my_students.append('spain')
# my_students.append('canada')
# my_students.append('nigeria')
# my_students.append('england')
# my_students.append('brazil')
# list_count = my_students.count('brazil')
# list_index = my_students.index('canada')
# print(list_index)
# print(my_students)
# list_copy = my_students.copy()
# list_copy.append('brazil')
# print(list_copy)
# list_pop = my_students.pop(2)
# print(list_pop)
# my_students.insert(2,'spain')
# my_students.insert(3,'canada')
# print(my_students)
# my_students.sort()
# print(my_students)
#
#
#
#
# #LOOP IN A LIST
#
#
# my_students = list()
# my_students.append('brazil')
# my_students.append('mexico')
# my_students.append('spain')
# my_students.append('canada')
# my_students.append('nigeria')
# my_students.append('england')
# my_students.append('brazil')
#
#
# for student in my_students:
#
#     print(student)
#
#
#
# # )
# # print(my_vowels)my_cong = ('congrats')
# # my_vowels = ('a','o')
# # my_consonants = ('c','n','g','r','t','s')
# # print(my_cong
# # print(my_consonants)
#
#
# vols = []
# cons = []
# cons = ['C','O','N','G','R','A','T','S']
# for c in cons:
#     if c== 'A' or c == 'E' or c == 'I' or c== 'O' or c== 'U':
#         vols.append(c)
#
#
# print(vols)
#
# for c in cons:
#     if c== 'C' or c == 'N' or c == 'G' or c== 'R' or c== 'T' or c== 'S':
#         cons.append(c)
#
# print(cons)
#
#
#




# #TUPLES IN SEQUENCE AND ITERIABLE


dom_anim= ('dog','cat', 'goat','rabbit','hen','cat', 'goat','cat', 'goat')
print(dom_anim)
tp_count= dom_anim.count('cat')
print(tp_count)

tp_index= dom_anim.index('cat',5,6)
print(tp_index)




#SETS IN SEQUENCE AND ITERIABLES


my_set = {'pencil','sharpener','carayon','pen','ruler'}
print(my_set)


my_set= set()
my_set.add('tiger')
my_set.add('lion')
my_set.add('cheater')
my_set.add('leopard')
my_set.add('jacquer')
my_set.add('leopard')
my_set.add('cheater')
print(my_set)



#SET METHODS API

countries_1 = {'togo','senegal','nigeria','ukarine','russia'}
countries_2 = {'togo','senegal'}

# countries_1.intersection_update(countries_2)
# print(countries_1)
set_diff = countries_1.difference(countries_2)
print(set_diff)

set_union= countries_1.union(countries_2)
print(set_union)

set_inter= countries_1.intersection(countries_2)
print(set_inter)

set_sub= countries_2.issubset(countries_1)
print(set_sub)


set_sup= countries_1.issuperset(countries_2)
print(set_sup)


set_joint= countries_1.isdisjoint(countries_2)
print(set_joint)



fruits= ('apple','orange','grape','pineapple','cashew')
froz_set= frozenset(fruits)
print(froz_set)


























































