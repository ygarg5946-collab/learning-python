#Creating classes in python new topic day-17
class User:
    pass

user_1=User()
#Pascal Case
# hey see the Pascal case meaning is the first letter of all the
#words must be capital
## The meaning of the camel case is that the first word has smaller
#case and other are capital
### snake_case=seprated by a underscore
user_1.id='001'
user_1.username='yash'
print(user_1.username)

user_2=User()
user_2.id='002'
user_2.username='angela'
print(user_2.username)
#now we will study about the constructor
#it is like that when we make a new object it specifies what to
# to do or take like that.....
# for constructing the constructor we will use the
#fucntion known as __init__()
