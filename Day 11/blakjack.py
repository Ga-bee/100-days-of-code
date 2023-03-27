import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
######## organizar e separar em funções

user = []
computer = []

def menu():
    print ('logo')

def check(user):
    """Checa se o usuário perdeu"""
    sum_user = sum(user)
    dif_user = 21 - sum_user    
    if dif_user < 0:
        print("You loose")
        return False
    elif dif_user > 0:
        
        return True
    
play = input('Would you like to play Blackjack? y or n\n')
while play == 'y': 
    #começa o loop do jogo
    user.append( random.choice(cards))
    computer.append(random.choice(cards))
    print(f'The first computer card is {computer[0]}')
    print(f'Your cards: {user}')
    checking = check(user)
    
    
    more_cards = input('Do you want another card? y or n\n').lower()
    if more_cards == 'y':
        if checking: 
            continue
        elif checking == False:
            print("DJ para o som")
            break
      
        
    elif more_cards == 'n':
        # se o usuario quiser parar de jogar
        
        sum_user = sum(user)
        dif_user = 21 - sum_user
        sum_computer = sum(computer)
        dif_computer = 21 - sum_computer

        #mapeando possibilidades de epate, perder

        #21
        if dif_user == 0:
            # mesa tbm faz 21
            if dif_computer == 0:
                print('Empate(pesquisar em ingles)')
            else:
                print(f'Your cards: {user}')
                print(f"Computer's cards: {computer}")
                print('You win!')
                break
        # passou de 21
        if dif_user < 0:
            print(f'Your cards: {user}')
            print(f"Computer's cards: {computer}")
            print("You loose")
            break
        
    
        elif dif_user > dif_computer:
            print(f'Your cards: {user}')
            print(f"Computer's cards: {computer}")
            print("You loose")
        elif dif_user < dif_computer:
            if sum_computer < 17:
                computer.append( random.choice(cards))
                if dif_user > (21-sum_computer):
                    print(f'Your cards: {user}')
                    print(f"Computer's cards: {computer}")
                    print("You loose")
                    break
                else:
                    print(f'Your cards: {user}')
                    print(f"Computer's cards: {computer}")
                    print("You win")

        # empate
        elif dif_user == dif_computer:
            print("Draw")
            computer.append( random.choice(cards))
            user.append( random.choice(cards))
            sum_user = sum(user)
            dif_user = 21 - sum_user
            sum_computer = sum(computer)
            dif_computer = 21 - sum_computer   
            if dif_user == 0:
            # mesa tbm faz 21
                if dif_computer == 0:
                    print(f'Your cards: {user}')
                    print(f"Computer's cards: {computer}")
                    print('Empate(pesquisar em ingles)')
                else:
                    print(f'Your cards: {user}')
                    print(f"Computer's cards: {computer}")
                    print('You win!')
                    break
            # passou de 21
            if dif_user < 0:
                print(f'Your cards: {user}')
                print(f"Computer's cards: {computer}")
                print("You loose")
                break
            elif dif_user > dif_computer:
                print(f'Your cards: {user}')
                print(f"Computer's cards: {computer}")
                print("You loose")
            elif dif_user < dif_computer:
                if sum_computer < 17:
                    computer.append( random.choice(cards))
                    if dif_user > (21-sum_computer):
                        print(f'Your cards: {user}')
                        print(f"Computer's cards: {computer}")
                        print("You loose")
                        break
                    else:
                        print(f'Your cards: {user}')
                        print(f"Computer's cards: {computer}")
                        print("You win") 


