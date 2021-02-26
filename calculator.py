'''
PASTE YOUR PSEUDOCODE
'''

def input_number(ordinal):
    number = float(input("Please enter the "+ordinal+" number: "))
    return number

def add(a,b):
    ans = a+b
    return ans

def menu():
    print("Welcome to the Amazing Calculator!")
    return int(input("Type 1 for add, 2 for subtract, 3 for multiply, 4 for divide or 0 to exit..."))

while True:
    choice = menu()
    if choice == 0:
        break
    num1 = input_number("first")
    num2 = input_number("second")
    num3 = input_number("third")
    if choice == 1:
        result = add(num1,num2)
    print("The result of your calculation is",result)
print("Thanks ever so much for using the calculator.")
