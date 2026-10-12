def add(first_number,second_number):
    return first_number+second_number
def subtract(first_number,second_number):
    return first_number-second_number
def multiply(first_number, second_number):
    return first_number*second_number
def division(first_number, second_number):
    return first_number/second_number
def calculation():
    first_number=int(input("What is your first number?"))
    second_number=int(input("What is your second number?"))
    print("Choose the operation you want to use: +,-,/,*")
    operation=input("What operation do you want to use?")
    while operation!="+" and operation!="-" and operation!="*" and operation!="/":
        print ("Invalid operation!")
        operation=input("Choose an operation from this list: +,-,/,*")
    if operation=="+":
        result=add(first_number,second_number)
        print(result)
    elif operation=="-":
        result=subtract(first_number,second_number)
        print(result)
    elif operation=="*":
        result=multiply(first_number,second_number)
        print(result)
    elif operation=="/":
        if second_number==0:
            print("Cannot divide by 0")
        else:
            result=division(first_number,second_number)
            print(result)
    else:
        print("Invalid operation!")
print("Choose yes or no")
answer=input("Do you want to do a calculation?").lower()
while answer!="no" and answer!="n":
    if answer=="yes" or answer=="y":
        calculation()
    else:
        print("Please choose yes or no")
    answer=input("Do you want to do a calculation?").lower()
print("Thank you for using the calculator!")