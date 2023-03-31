from menuCoffee import Menu, MenuItem
from coffeeMAker import CoffeeMaker
from moneyMachine import MoneyMachine


menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input(f"Welcome to the coffee machine. What would you like to order? \n{menu.get_items()}")
    if choice == 'off':
        break
    elif choice == 'report':
        print(coffe_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if  coffe_maker.is_resource_sufficient(drink):
            # print(drink + )
            money_machine.make_payment(drink.cost)
            coffe_maker.make_coffee(drink)

    




