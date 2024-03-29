
#addizione
def add(n1, n2):
    return n1 + n2

#sottrazione
def subtract(n1, n2):
    return n1 - n2

#moltiplicazione
def multiply(n1, n2):
    return n1 * n2

#divisione
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

def calculator():
    
    num1 = float(input("What's the first number?:\n"))

    for key in operations:
        print(key)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?:\n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)


    #if operation_symbol == "+":
    #    answer = num1 + num2
    #elif operation_symbol == "-":
    #    answer = num1 - num2
    #elif operation_symbol == "*":
    #    answer = num1 * num2
    #else:
    #    answer = num1 / num2

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else: 
            should_continue = False
            calculator()
            
calculator()
    
    
    