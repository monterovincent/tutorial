#MAPPING IN FUNCTION


my_nums = [1,2,3,4,5]
map_list = map(lambda x: x^2,my_nums)
print (list(map_list))



my_nums2 = [1,2,3,4,5]
map_list2 = map(lambda x: x*2,my_nums2)
print (list(map_list2))





my_nums3 = [1,2,3,4,5]
map_list3 = map(lambda x: x+2,my_nums3)
print (list(map_list3))





#FILTERING IN FUNCTION LAMBDA


tp = (23,12,13,24,25,45,19)

filt_data = filter(lambda x : x%2==0,tp)
print(tuple(filt_data))


t = ['k','ol','bro','rety','devop','loop']
t_data = filter(lambda x: x.__contains__('o'),t)
print(list(t_data))


















