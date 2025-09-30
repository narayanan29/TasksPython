#calculator
def addition(n1,n2):
    return n1+n2
def substraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

operations={
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division,
}
should_acumlate=True
num1=float(input("Enter first number:"))
while should_acumlate:
    for symbol in operations:
        print(symbol)
    operator=input("Enter the operator: ")
    num2=float(input("Enter the second number: "))
    answer=operations[operator](num1,num2)
    print(f"{num1} + {num2} = {answer}")

    choice=input("Would you like to continue? (y/n): ")

    if choice=="y":
        num1=answer
    else:
        should_acumate=False
        print("\n"*50)