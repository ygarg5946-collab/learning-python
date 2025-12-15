class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.username=user_name
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1


# user_1=User('001','yash')
# print(user_1.id)
# print(user_1.username)
# user_2=User('002','angela')
# print(user_2.id)
# print(user_2.username)
# print(user_2.followers)
user_1=User('001',"yash")
user_2=User('002',"angela")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#see there is a open trivia database from
#we can get many question taught by madam in last lecture of the day-17