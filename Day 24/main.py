# import os
# dir = os.getcwd()
# dirs  = os.listdir()
# os.chdir(dir)




# file = open("Day 24/file.txt")

# contents = file.read()

# print(contents)

# file.close()

########### WE SHOULD ALWAYS CLOSE OUR FILES #######################
########### WE CAN USE ALSO THE NEXT WAY SO THE FILE IS CLOSED AUTOMATICALY##############
with  open("Day 24/file.txt", mode= 'r') as file:
    file.read()

###to write
with  open("Day 24/file.txt", mode= 'a') as file:
    file.write("\nGabee is actualy my nickname, my name is Gabriela.")


with  open("Day 24/new_file.txt", mode= 'w') as file:
    file.write("\nTesting")
