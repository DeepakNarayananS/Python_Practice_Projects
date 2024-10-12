# Coding a Simple Calculator 

def operands(number):
    while True:
        value=input("Enter the operand " + str(number) + ": " )
        try:
            return float(value)
        except:
            print("The entered operands should be in number format , you have typed a wrong format modify it to the right one.....")

first_operand = operands(1)
second_operand = operands(2)

sign = input("Enter the operation sign which needs to be performed (add(+) , sub(-) , mul(*) , div(/) , power(**) , modulus(%)) : ")

output1 = int(first_operand)
output2 = int(second_operand)

print(f"{output1} {sign} {output2}")

result=0

if sign=="+":
    result = first_operand + second_operand    
elif sign=="-":
    result = first_operand - second_operand    
elif sign=="*":
    result = first_operand * second_operand 
elif sign=="/":
    if second_operand!=0:
        result = first_operand / second_operand
    else:
        print("Division by zero is not allowed. change the second operand value.")
elif sign=="**":
    result = first_operand ** second_operand
elif sign=="%":
    if second_operand!=0:
        result=first_operand % second_operand
    else:
        print("Modulus by zero is not allowed. change the second operand value.")
else:
    print("The provided sign is invalid , please try again.....")

print(result)