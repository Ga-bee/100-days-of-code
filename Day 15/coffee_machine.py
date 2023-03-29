MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "Pennies": 0.01,
    "Dimes": 0.10,
    "Quarters": 0.25,
    "Nickels": 0.05
}

   
def buy(coffee):
    if coffee == "cappuccino":
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
        #ve
    if coffee == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 100
        #ve
    if coffee == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        
        #ve

def check_resources(type):
    
    coffee = MENU[type]['ingredients']['coffee']
    water = MENU[type]['ingredients']['water']
    milk = MENU[type]['ingredients']['milk']

    if resources["coffee"] < coffee or resources["water"] < water or resources["milk"] < milk:
        if resources["coffee"] < coffee:
            print("Sorry we're out of coffee. Please comeback latter.")

        if resources["water"] < water:
            print("Sorry we're out of water. Please comeback latter.")

        if type != 'espresso':
            if resources["milk"] < milk:
                print("Sorry we're out of milk. Please comeback latter.")
        return False
    return True

while True:
    print("Welcome, to the coffee machine. What would you like to order?")
    coffee = input("espresso/latte/cappuccino\n")
    if coffee == 'report':
        print(resources)
        print(f'Profit: {profit}')
    
    
    else:    
        check = check_resources(coffee)

        if check == True:
            
            price = MENU[coffee]['cost']
            print(f"{coffee} costs {price}")
            print("Please insert coins.")
            quarter = int(input("How many quarters?"))* coins['Quarters']
            dime = int(input("How many dimes?"))* coins['Dimes']
            nickel = int(input("How many nickels?"))* coins['Nickels']
            penny = int(input("How many pennies?"))* coins['Pennies']
            payment = quarter + dime + nickel + penny

            if payment < price:
                print('Not enough money. Money refunded.')
                continue
            
            elif payment == price:
                profit += payment
                print("Here's your coffee.")
                buy(coffee)

            elif payment > price:
                profit += price
                print("Here's your coffee.")
                print(f"Here's the change:  {(payment - price):.2}")
                buy(coffee)

        elif check == False:
            break
