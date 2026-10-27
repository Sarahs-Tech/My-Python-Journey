expenses = [
    {"category": "Food", "amount": 35.50},
    {"category": "Transport", "amount": 12.00},
    {"category": "Food", "amount": 24.50},
    {"category": "Entertainment", "amount": 40.00},
    {"category": "Transport", "amount": 8.00}
]

def analyse_expenses(expenses):
    total=0
    most=expenses[0]
    category_totals={}
    ind_cats={}

    for exp in expenses:
        total=total+exp["amount"]
        if most["amount"]<exp["amount"]:
            most=exp

        if exp["category"] not in category_totals:
            category_totals.update({exp["category"]:exp["amount"]})
        else:
            category_totals[exp["category"]]+=exp["amount"]

        if exp["category"] not in ind_cats:
            ind_cats.update({exp["category"]: 1})
        else:
            ind_cats[exp["category"]]+=1

    frequent=0
    frequent_cat=[]
    for x, y in ind_cats.items():
        if frequent<y:
            frequent=y
            frequent_cat=[x]
        elif frequent==y:
            frequent_cat.append(x)
    

    nums=len(expenses)
    average=round(total/nums,2)
    return total, most, nums, average, category_totals, ind_cats, frequent, frequent_cat

total, most, nums, average, category_totals, ind_cats, frequent, frequent_cat=analyse_expenses(expenses)

above=[]
for exp in expenses:
    if exp["amount"]>average:
        above.append(exp)



print(f"Total spent: £{total:.2f}")
print(f"Number of expenses: {nums}")
print(f"Most expensive expense: {most['category']}- £{most['amount']:.2f}")
print(f"Average expense: £{average:.2f}")
# print(category_totals)

print(above)
for cat in above:
    print(f"{cat['category']}- £{cat['amount']:.2f}")

print(ind_cats)
print(f"{frequent_cat}:{frequent}")

# Find any requested category in any given list:

def filter_by_category (expenses, requested_cat):
    requested_list=[]
    for exp in expenses:
        if exp["category"]==requested_cat:
            requested_list.append(exp)
    return requested_list

result=filter_by_category(expenses, "Food")
print(result)

# filter expenses above the given minimum in a given list:

def filter_expenses_above (expenses, minimum):
    expenses_above=[]
    for exp in expenses:
        if exp["amount"]>minimum:
            expenses_above.append(exp)

    return expenses_above
result=filter_expenses_above(expenses, 20)
print(result)


with open("expenses.txt", "w") as file:
    for exp in expenses:
        file.write(f"{exp['category']}: £{exp['amount']}\n")

# with open("expenses.txt") as file:
#     print(file.read())


with open("expenses.txt", "r") as file:
    total=0
    for line in file:
        new_list=line.strip().split("£")
        amount=float(new_list[1])
        total+=amount

    print(f"Total expenses: £{total:.2f}")


# ask user for a category and its expense and append that to the expenses.txt file:

new_cat=input("Enter the new expenses category?")
new_amount=float(input("Enter the amount"))

with open("expenses.txt", "a") as file:
    file.write(f"{new_cat}: £{new_amount:.2f}\n")

with open("expenses.txt", "r") as file:
    print(file.read())