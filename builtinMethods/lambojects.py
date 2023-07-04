#LAMBDA OBJECTS IN FUNCTIONS USED IN MAPPING

# students= [
#     { 'name': 'john doe',
#       'father name': 'robert doe',
#       'address': '123 hall street'
#
#     },
#
#
#
#     {'name': 'kalu mary',
#      'father name': 'luke mary',
#      'address': '127 brain street'
#
#      },
#
#
#
#     {'name': 'kane moon',
#      'father name': 'france moon',
#      'address': '167 greek street'
#
#      }
# ]
# stu_ups = map(lambda stu : stu['name'], students)
# stu_ = list(stu_ups)
# print(stu_)


#MAPPING SALARY SCALE UP CODE BELOW WITH LAMBDA FUNCTION AFTER BEING PUT IN A LIST FIRST

students= [
    { 'name': 'john doe',
      'father name': 'robert doe',
      'address': '123 hall street',
      'salary' : 698000,
      'age' : 33


    },



    {'name': 'kalu mary',
     'father name': 'luke mary',
     'address': '127 brain street',
     'salary' : 3980000,
     'age' : 45

     },



    {'name': 'kane moon',
     'father name': 'france moon',
     'address': '167 greek street',
     'salary' : 4580000,
      'age' : 55


     }
]
stu_ups = map(lambda stu : stu['salary'], students)
sal = list(stu_ups)
print(sal)

# my_sal = ('salary')
sal_list = map(lambda s: s + s*0.05,sal)
res = list(sal_list)
print(res)
# print (list(map_list))




