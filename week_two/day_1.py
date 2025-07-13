#dictionary

dictionary = {
    "key" : "value"
}

person = {
    "name" : "Mistura",
    "age" : 15,
    "gender" : "Female",
    "nationality" : "Nigeria",
    "religion" : "Islam",
    "extra_details" : {
    "nin" : 1334678908765,
    "bvn" : 5678921762627,
    "date_of_birth" : '12 Nov 1997',
    }
}

# print(person ["extra_details"] ["nin"])

person["name"] = "Segun"
person["height"] = "1.65"

# print(person)

data = {}

print("empty:", data)

data["mine"] =25
data["age"] =28

print( "second:", data)

#deleting a value

del data["age"]
print( "third:", data)

data.clear()

print( "deleting:", data)


#LIST

collection = ["Abel", "Kane", 23, 145.4, True, [1, "tame", 14, ["Tomi",42 ]]]

# print(collection[-1][-1][0])
# print(collection[5][3][0])

collection.insert(0, "Arsenal") #Add a value to a specific index
collection.pop(4) #Takes out a value with a specific index
collection.remove(True) #Takes out a value by writing out the value
collection[0] = "Liverpool" #Update a value
# print(collection)

#Membership
#in - boolean

checks = "Arsenal" in collection

print(checks)

#Concatenation

concat_list = [1,2,3,4,5] + [6,7,8,9,0]
print(concat_list)

#Repetition

item = ["Hi"]
repeat_list = item * 5

print(repeat_list)

#Length - uses len to check the length of a list
print(len(concat_list))

#Slicing 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

slice_items = numbers[-4:]
# print(slice_items)

numbers.append(16)
numbers.insert(14, 8)
print(numbers)

# Control structure part 1 - if statement

num = 1
if num > 2:
    print("is greater")

elif num == 1:
    print("is greater to 3")

else:
    print("is not greater")