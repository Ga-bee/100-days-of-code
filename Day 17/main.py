class User:
    def __init__(self,username,id) -> None:
       print("new user has been created...")
       
       self.username = username
       self.id = id
       self.followers = 0
       self.following  = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
   

from prettytable import PrettyTable


user_1 = User('gabriela',1)
user_2 = User('camila',2)
user_3 = User('esther',3)

user_1.follow(user_2)
table = PrettyTable()

table.add_column('id',[user_1.id,user_2.id,user_3.id])
table.add_column('username',[user_1.username,user_2.username,user_3.username])
table.add_column('following',[user_1.following,user_2.following,user_3.following])
table.add_column('followers',[user_1.followers,user_2.followers,user_3.followers])

table.align ='l'

print(table)
