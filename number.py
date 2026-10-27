# Read user input until they entered a valid number
def read_number():
    need_input = True

    while need_input:
        try:
            num = int(input("input number: "))
            need_input = False
        except ValueError:
            print("invalid, try again")   

# read_number() 

def read_number2():
    valid = False

    while not valid:
        try:
            num = int(input("input number: "))
            valid = True
        except ValueError:
            print("invalid, try again") 

def read_number3():
    while True:
        try:
            num = int(input("input number: "))
            break
        except ValueError:
            print("invalid, try again")

def read_valid_number():
    while True:
        try:
            num = int(input("input number: "))
            return num
        except ValueError:
            print("invalid, try again")

# Read a valid number from the user but try at most N times.
def read_valid_number_max(max_tries):
    tries = 0
    
    while tries < max_tries:
        try:
            num=int(input("input a number:"))
            return num
        except ValueError:
            print("invalid, try again")
        tries += 1

# Read a valid number from the user but try at most N times.
def read_valid_number_max2(max_tries):
    while max_tries > 0:
        print(max_tries)
        try:
            num=int(input("input a number:"))
            return num
        except ValueError:
            print("invalid, try again")
        max_tries -= 1
        




def read_valid_number_max3(max_tries):
    if max_tries<=0:
        print("invalid")
        return
    while max_tries>0:
        try:
            num=int(input("Input number:"))
            return num
        except ValueError:
            print("Invalid, try again!")
        max_tries-=1



# Print numbers from A until B
def print_nums(A,B):
    while A<=B:
        print(A)
        A+=1
        



# Print numbers from B to A (reverse)
def print_nums2(A,B):
    while B>=A:
        print(B)
        B-=1


# Print numbers from A to 0 (excluding 0)
def print_nums3(A):
    while A!=0 :
        print(A)
        if A>0:
            A-=1
        elif A<0:
            A+=1
        
# print_nums3(4)

# Print numbers from 0 to A (including A)
def print_nums4(A):
    while 0<=A:
        print(A)
        A-=1
