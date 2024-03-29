
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

num1 = int(input("What's the first number?:\n"))

for key in operations:
    print(key)
    
operation_symbol = input("Pick an operation for the list above: ")

num2 = int(input("What's the second number?:\n"))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)

#if operation_symbol == "+":
#    answer = num1 + num2
#elif operation_symbol == "-":
#    answer = num1 - num2
#elif operation_symbol == "*":
#    answer = num1 * num2
#else:
#    answer = num1 / num2
    
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation for the list above: ")
num3 = int(input("What's the next number?:\n"))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1,num2), num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")