people1 = [
    {"name": "Sarah", "age": 28, "gender":"female", "city":"London"},
    {"name": "Ali", "age": 32, "gender":"male", "city":"Berlin"},
    {"name": "Emma", "age": 25, "gender":"female", "city":"Shiraz"}
]
people2 = [
    {"name": "Jack", "age": 27, "gender":"male", "city":"Bath"},
    {"name": "Jill", "age": 34, "gender":"female", "city":"Bristol"},
    {"name": "Anna", "age": 20, "gender":"female", "city":"Brighton"}
]





def find_oldest(peps, gen):
    oldest=peps[0]
    for person in peps:
        if oldest["age"]<person["age"] and person["gender"]==gen:
            oldest=person
    return oldest 
# result=find_oldest(people1, "female")
# print(result)






def find_yougest(list, gen, cit):
    if len(list) == 0:
        return None

    youngest=None
    for person in list:
        if  (youngest is None or youngest["age"]>person["age"]) and person["gender"]==gen and person["city"]==cit:
            youngest=person
    return youngest
# result=find_yougest(people2, "female", "Bristol")
# print(result)






def find_n(nums, target):
    found = False
    for n in nums:
        if n == target:
            found = True
    return found






food=input("What are your three favourite food? separated by commas:")
food_list=food.split(",")
clean_food=[]
for food_name in food_list:
    clean_food.append(food_name.strip())
# print(clean_food)




# return, returns the value and jums out of the function. So, annything after return won't be executed!
def myfunction():
  return 3+3
  print("Hello, World!")

print(myfunction())