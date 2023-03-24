def add(num1,num2):
    """Add two numbers given as inputs"""
    return num1 + num2

def sub(num1,num2):
    """substract two numbers given as inputs"""
    return num1 - num2

def mult(num1,num2):
    """multipy two numbers given as inputs"""
    return num1 * num2

def div(num1,num2):
    """divide two numbers given as inputs"""
    return num1 / num2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div
}
from logo import logo
def loop(num2):

    for symbol in operations:
        print(symbol)

    symbol_operations = input("Pick an operation from the line above:")
    answer =  operations[symbol_operations](num2)

    print(f'{num_1} {symbol_operations} {num2 } = {answer}')
    return answer
print(logo)
num_1 = float(input("What's the first number?"))

while True:
    call_loop = loop(float(input("What's the next number?")))
    keep = input(f"Type 'y' for continue calculating with {call_loop} or 'n' to stop.")
    if keep == 'y':
        continue
    elif keep == 'n':
        break