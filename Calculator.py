def add(first_number,second_number):
    return first_number+second_number
def subtract(first_number,second_number):
    return first_number-second_number
def multiply(first_number, second_number):
    return first_number*second_number
def division(first_number, second_number):
    try:
        return first_number/second_number
    except ZeroDivisionError as error:
        return error
def calculation():
    def read_valid_input():
        while True:
            try:    
                first_number=int(input("What is your first number?"))
                operation=input("Choose an operation from: +,-,*,/")
                if operation not in ["+", "-", "*", "/"]:
                    raise ValueError ("Choose a valid operation from: +,-,*,/")
                second_number=int(input("What is your second number?"))
                return first_number, operation, second_number
            except ValueError as error:
                print(error)
                print()
                
    first_number, operation, second_number=read_valid_input()

    match operation:
        case  "+":
            result=add(first_number, second_number)
            print(result)
        case "-":
            result=subtract(first_number, second_number)
            print(result)
        case "*":
            result=multiply(first_number, second_number)
            print(result)
        case "/":
            result=division(first_number, second_number)
            print(result)

answer=input("Do you want to run a calculation?").lower()
while answer!="no" and answer!="n":
    if answer=="yes" or answer=="y":
        calculation()       
    else:
        print("Choose yes or no")
    answer=input("Do you want to run a calculation?").lower()

print("Thank you for using this calculation!")


















#     print("Choose the operation you want to use: +,-,/,*")
#     operation=input("What operation do you want to use?")
#     while operation!="+" and operation!="-" and operation!="*" and operation!="/":
#         print ("Invalid operation!")
#         operation=input("Choose an operation from this list: +,-,/,*")
#     if operation=="+":
#         result=add(first_number,second_number)
#         print(result)
#     elif operation=="-":
#         result=subtract(first_number,second_number)
#         print(result)
#     elif operation=="*":
#         result=multiply(first_number,second_number)
#         print(result)
#     elif operation=="/":
#         if second_number==0:
#             print("Cannot divide by 0")
#         else:
#             result=division(first_number,second_number)
#             print(result)
#     else:
#         print("Invalid operation!")
# print("Choose yes or no")
# answer=input("Do you want to do a calculation?").lower()
# while answer!="no" and answer!="n":
#     if answer=="yes" or answer=="y":
#         calculation()
#     else:
#         print("Please choose yes or no")
#     answer=input("Do you want to do a calculation?").lower()
# print("Thank you for using the calculator!")
