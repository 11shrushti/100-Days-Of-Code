logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



#Function for the add
def add(n1,n2):
    return n1+n2
# sub
def sub(n1,n2):
    return n1-n2
# mutiply
def multiply(n1,n2):
    return n1*n2
# divide
def divide(n1,n2):
    return n1/n2

# Dictionaries named operations
operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number?"))
    # looping through the dictionaries
    for x in operations:
        print(x)

    should_continue = True
    while should_continue:
        operation_symbols = input("Pick an operation :")
        num2 = float(input("What is the next number?"))
        calculation_operation = operations[operation_symbols]
        answer = calculation_operation(num1,num2)
        print(f"{num1} {operation_symbols} {num2}={answer}")   

        if input(f"Type 'y'to continue the calcualtion with {answer} or type'n' to start a new calculations:").lower()=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()




