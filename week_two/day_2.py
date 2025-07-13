# Tuple

a_tuple = ("red", "blue" , "yellow") # Immutable
# print(a_tuple)
# print(type(a_tuple))

# a_tuple[0] = "green"
# print(a_tuple)   # Cannot be changed

#Repetition
a = ("Hi")
tuple1 = a * 3
# print(tuple1)

#Membership

check_value_in_tuple = "blue" in a_tuple
# print(check_value_in_tuple)

#Concatenation
concat = (1,2,3,4) + (5,6,7,8)
# print(concat)

# Slice a value in tuple

tuple3 = (11,12,13,14,15,16)

slicing = tuple3[2:5]
# print(slicing)

#check for len in tuple

# print(
#     len(tuple3)
# )

val = "Hammed", #still a tuple
# print(val)

#Set - Unordered data structure - A collection of unordered data

unordered_values = {"Lagos", "Rivers", "Abuja", "Kogi"}
unordered_values_1 = {"Delta", "Oyo", "Lagos", "Kogi","Sokoto"}

# print(
#     unordered_values
# )

# membership
check_value_in_set = "Rivers" in unordered_values
# print(check_value_in_set)

unordered_values.add("Zamfara") #Add value to set
unordered_values.remove("Abuja") #Remove value from set
unordered_values.update(["Abuja", "Adamawa", "Akwa Ibom"]) #Update value in a set

# print(
#     unordered_values
# )

#Union 
merge = unordered_values.union(unordered_values_1) #unordered_value | unordered_value_1 and you can't have duplicate value in a merge

# print(
#     merge
# )


#Intersection
intersect = unordered_values.intersection(unordered_values_1) #unordered_values & unordered_values_1

# print(
#     intersect
# )

#Set does not have duplicates value inside a set

#Loop - Repeat a block of code until a condition is met

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# for item in list:
#     print(item)
#     if item == 8:
#         print("8 is in here,stop the loop")
#         break


menu = ["beans", "plantain", "rice", "pasta", "macaroni", "mashed potatoes", "afang soup", "salad"]

new_menu = [
    {
        "name" : "rice",
        "price" : 2000
    },
    {
        "name" : "beans",
        "price" : 5000
    },
    {
        "name" : "pasta",
        "price" : 7000
    }
]

# order_food = input("Hello. what do you want to order?: ")

# for dish in new_menu:
#     if order_food == dish["name"]:
#         print(f"Here is your {dish["name"]}, that would be {dish["price"]} naira")
#         break
# else:
#         print("You have not made an order")


# for dish in menu:
#     if order_food == dish:
#         print(f"Here is your{dish}, that would be 1000 naira")
#         break
#     else
#         print("You have not made an order")

# For loop doesn't work with an empty list or an iterable

# store= ["Books"]
# for obj in store:
#     if len(store) < 5:
#         obj = input("What object do you want to add to store?: ")
#         store.append(obj)
#         print(store)
    
# else:
#     print("You have exceeded your limit")

# num = 0

# while num < 10:
#     num = num + 1
#     print("Keep running", num)

# while

num = 20
while True:
    guess = int(input("Guess the number: "))
    if guess > num and guess <= 25:
        print("You are too close!")
    elif guess > num:
        print("Number is greater than the guess number")
    elif guess < num and guess >= 15:
        print("Almost there. Don't give up!")
    elif guess == num:
        print(f"Hurray, you have found the number. The number is {num}")
        break
    else:
        print("Number is lesser than the guess number")





