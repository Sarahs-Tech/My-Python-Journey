#variable and if elif else conditions

# name=input("What is your name?")
# age=int(input("How old are you?"))

# if age<18:
#     # print(f"Hello {name}, You are a minor.")

# elif 18<=age<64:
#     # print(f"Hello {name}, You are an adult.")

# else:
    # print(f"Hello {name}, You are a senior.")

# def get_numbers():
#     return [1,2,3]

# write all numbers from 1 to n & calculate the sum of all numbers

# def nums(m):
#     sum=0
#     for n in range(1,m+1):
#         print(n)
#         sum=sum+n
#     return sum

# result=nums(4)
# print(result)



# def num(m):
#     n=1
#     sum=0
#     while n<=m:
#         print(n)
#         sum=sum+n
#         n=n+1
#     return sum

# result=num(4)
# print(result)



#find all the numbers that are more or equal to 10,
#Count them, and find their total.
# numbers = [12, 7, 25, 4, 18, 31, 10, 3]

# count=0
# sum=0

# for n in numbers:

#     if n>=10:
#         print(n)
#         count=count+1
#         sum=sum+n
#         print(count)
#         print(sum)


#You should be able to give the program any list you want (not a fixed list).
#find all the even numbers, count them, find the total.

# def analyse_numbers(numbers):
#     count=0
#     sum=0
#     for n in numbers:
#         if n % 2==0:
#             count=count+1
#             sum=sum+n
#     return sum, count

# sum, count =analyse_numbers([3, 8, 12, 5, 7, 10, 15, 20])
# print("Even numbers count:", count)
# print("Even numbers total:", sum)




# find the employee with highest salary, how many employees earn more thank 35000 a year?,
# average salary of all employees

# def analyse_salaries(employees):
#     highest_salary=employees[0]
#     count=0
#     total=0
#     for person in employees:
#         if highest_salary["salary"] < person["salary"]:
#             highest_salary=person
#         if person["salary"]>35000:
#             count=count+1
#         total=total+person["salary"]
#         average_salary=round(total/len(employees))
#     return highest_salary, count, total, average_salary

# employees = [
#     {"name": "Sara", "salary": 30000},
#     {"name": "Ali", "salary": 42000},
#     {"name": "Mina", "salary": 35000},
#     {"name": "David", "salary": 50000},
#     {"name": "Reza", "salary": 28000}
# ]

# highest_salary, count, total, average_salary=analyse_salaries(employees)

# print(f"Highest paid employee:{highest_salary['name']}, £{highest_salary['salary']}")
# print("Employees earn more than £35000:", count)
# print(f"Average salary: £{average_salary}")





# find product with highest price, count how many products are in stock,
# total inventory value, number of product types that are in stock,
# create a list of the names of procucts that are out of stock

# products = [
#     {"name": "Laptop", "price": 900, "stock": 4},
#     {"name": "Mouse", "price": 25, "stock": 0},
#     {"name": "Keyboard", "price": 75, "stock": 8},
#     {"name": "Monitor", "price": 250, "stock": 3},
#     {"name": "USB cable", "price": 10, "stock": 0}
# ]

# expensive=products[0]
# stock=0
# type_stock=0
# item_value=0
# no_stock=[]

# for item in products:
#     if expensive["price"]<item["price"]:
#         expensive=item
#     stock=stock+item["stock"]
#     if item["stock"]>0:
#         type_stock=type_stock+1
#     item_value=item_value + item["price"]*item["stock"]
#     if item["stock"]==0:
#         no_stock.append(item["name"])

# print(f"The product with highest price is: {expensive['name']}")
# print(f"Current stock is: {stock}")
# print(f"Number of product types in stock: {type_stock}")
# print(f"Total inventory value: {item_value}")
# print(f"Products that are out of stock: {no_stock}")



# shopping=[]

# products=input("Enter a product!").lower()
# while products!="done":
#     shopping.append(products)
#     products=input("Enter a product!").lower()
# print(f"You added {len(shopping)} products.")
# print(shopping)



# shopping=[]

# while True:
#     products=input("Enter a product!").lower()
#     if products== "done":
#         break
#     shopping.append(products)

# print(f"You added {len(shopping)} products.")
# print(shopping)



# shopping=[]

# finish=False
# while not finish:
#     products=input("Enter a product!").lower()
#     if products!= "done":
#         shopping.append(products)
#     else:
#         finish=True

# print(f"You added {len(shopping)} products.")
# print(shopping)
      



# find the average score of each student, 
# find the student with highest average,
# how many students passed (average>60), 

# students = [
#     {"name": "Sara", "scores": [78, 85, 92]},
#     {"name": "Ali", "scores": [45, 55, 60]},
#     {"name": "Mina", "scores": [90, 95, 88]},
#     {"name": "David", "scores": [35, 40, 48]},
#     {"name": "Reza", "scores": [65, 70, 72]}
# ]


# highest_average=0
# highest_person=""
# count=0

# for person in students:
#     # print(person["scores"])
#     total=0
    
#     for score in person["scores"]:
#         total=total+score
#     average=round(total/len(person["scores"]), 2)
#     if average>=60:
#         count=count+1
#     print(f"{person['name']}'s average: {average}")

#     if highest_average<average:
#         highest_average=average
#         highest_person=person["name"]
    
# # print(count)
    
# print(f"{count} students passed.")
# print(f"Highest scoring student is {highest_person}")
# print(f"Highest average is {highest_average}.")




