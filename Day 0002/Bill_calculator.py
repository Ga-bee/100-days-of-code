while True:
    try:
        total_bill = float(input('Please enter the total of the bill. \n$'))
        
        while True:
            tip = int(input('Porcentage of the tip. 10, 12 or 15.'))
            if tip ==10 or tip == 12 or tip == 15:
                break
            else:
                print('We just accept the following values:10, 12 or 15. Try again. ')

        people = int(input('How many people will split the bill?'))
        
        print(f'{(total_bill+(total_bill*tip/100))/people}')
        break
    except ValueError:
        print('Invalid value. Please try again.')
        continue

# try:
#     total_bill = float(input('Please enter the total of the bill. \n$'))
#     tip = int(input('Porcentage of the tip. 10, 12 or 15.'))
#     people = int(input('How many people will split the bill?'))
    
#     print(f'{(total_bill+(total_bill*tip/100))/people}')
# except ValueError:
#     print('Valor inválido inserido, por favor tente novamente.')
    
