import math


print("Select Operator")
print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sin")
print("cos")
print("tan")
print("cotan")
print("sqrt")
print("factorial")


op = input("Enter Operator: ")


op_list_two_arg = ["+","-","*","/"]
op_list_one_arg = ["sin","cos","tan","cot"]
op_list_other = ["sqrt","factorial"]

if op in op_list_two_arg:
   
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    if op=='+':
        result = a + b
    elif op=='-':
        result = a - b
    elif op=="*" :
        result = a * b
    elif op=="/":
        if b==0:
            result = "Not a Number"
        else:
            result = a / b
    
elif op in op_list_one_arg:


    a = float(input("Enter First Number: "))
    rad = math.radians(a)

    if op=='sin':
        result = math.sin(rad)
    if op=='cos':
        result = math.cos(rad)
    if op=='tan':
        result = math.tan(rad)
    if op=='cot':
        result = 1/math.tan(rad)

elif op in op_list_other:
    
    if op=="factorial":
 
        a = int(input("Enter First Number: "))
        result = math.factorial(a)
    elif op=="sqrt":
        
        a = float(input("Enter First Number: "))
        result = math.sqrt(a)

print(result)
