def treasure_chest():

    return print('''
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_''')
def game_over():
    print('''
                                                                                                                      
  ,ad8888ba,        db        88b           d88 88888888888      ,ad8888ba,  8b           d8 88888888888 88888888ba   
 d8"'    `"8b      d88b       888b         d888 88              d8"'    `"8b `8b         d8' 88          88      "8b  
d8'               d8'`8b      88`8b       d8'88 88             d8'        `8b `8b       d8'  88          88      ,8P  
88               d8'  `8b     88 `8b     d8' 88 88aaaaa        88          88  `8b     d8'   88aaaaa     88aaaaaa8P'  
88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""        88          88   `8b   d8'    88"""""     88""""88'    
Y8,        88  d8""""""""8b   88   `8b d8'   88 88             Y8,        ,8P    `8b d8'     88          88    `8b    
 Y8a.    .a88 d8'        `8b  88    `888'    88 88              Y8a.    .a8P      `888'      88          88     `8b   
  `"Y88888P" d8'          `8b 88     `8'     88 88888888888      `"Y8888Y"'        `8'       88888888888 88      `8b  ''')
    print("""               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#""")
    return
def you_win():
    print('''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░███░█▀▄▄▀█░██░███░███░██▄██░▄▄▀█░██
██▄▀▀▀▄█░██░█░██░███▄▀░▀▄██░▄█░██░█▄██
████░████▄▄███▄▄▄████▄█▄██▄▄▄█▄██▄█▀██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
    
    return

treasure_chest()
print("Welcome adventure, to the TREASURE ISLAND!!!\nYour mission is to find the old missing treasure.\nDo you think you can make it? \n I know you can, so lets begin. ")

direction = str(input("You're stepping out the door, you see a forest, wich direction are you gonna follow? Left or Right?")
                )

if direction.lower() == 'left':
    action = input("After a long walk you see a river. It's not deep, you could cross it. Will you try to Swim or Wait?")
    
    if action.lower() == 'wait':
        door = input('After some minutes ou start to feel sleepy, things are stange. A white fog? \nSuddenly three doors rise up on water. You should enter one. wich one? Yellow, Blue or Red? ')
        if door.lower() == 'yellow':
            print("You walk into the door, it's dark in there, the door start to close and locks you in. \nYou walk a little bit, and start to see a shine, you go closer. With your open streched arms you feel something, it's moving, you can open . \n It shine brighter! Congrats, you've found the TREASURE CHEST!")           
            treasure_chest()
            you_win()
        elif door.lower() == 'blue':
            print("You walk into the door, it's dark in there, the door start to close and locks you in. \nYou hear a sound, it's getting louder and close. A BITTE! The beasts start to atack you.")
            game_over()
        elif door.lower() == 'red':
            print("You walk into the door, it's hot and dark in there, the door start to close and locks you in. \n It's getting hotter, you start to burn.")
            game_over()

        else:
            print('You have waited too much.')
            game_over()
    elif action.lower() != 'wait':
        print("You try to swim, you're doig great. There is just the half of the way left. \nWait!? What is it? A CROCODILE! It is making some noise, and going under you. You're stuck, the crocodie is taking you under water.  ")
        game_over()
elif direction.lower() != 'left':
    print("what's this? A fog? It is too dark... Oh no, you are sufocating. ")
    game_over()
    