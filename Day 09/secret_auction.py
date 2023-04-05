# import replit
# import os
#  não consigo limpar o terminalll
def start():
    logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    print(logo)
    
# dicionari apaga anterior
registers = {}
finished = False
while finished == False:
    data = start()
    name = input("What's your name? \n")
    bid = int(input("What's your bid? \n$"))
    registers[name] = bid
    new = input("There are other users that want to bid? 'Yes' or 'No'.").lower()
    bigger = 0
    winner = ''
    if new == 'yes':
        #os.system('clear')
        continue
    if new == 'no':
        for k,v  in registers.items():
            print(k)
            if v > bigger:
                bigger = v
                winner = k

        print(f'The winner is {winner}')
        print(registers)

        
        break
    

