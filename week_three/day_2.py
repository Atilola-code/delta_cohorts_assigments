from functools import reduce

# Functions are block of codes that perform specific tasks

def a_function():
    return

def adding_two_numbers():
    first_number = 2
    second_number = 5
    add = first_number + second_number
    return add
# print(
#     adding_two_numbers(),
#     adding_two_numbers()
# )

     #OR
    #  return 2 + 5
def subtraction_of_numbers():
    first_number = 8
    second_number = 3
    subtract = first_number - second_number
    return subtract
# print(
#     subtraction_of_numbers()
# )

def multiplication_of_numbers():
    return 8 * 6
# print(
#     multiplication_of_numbers()
# )

def returns_a_string():
    str = "coding is life and the future"
    return str
# print(
#     returns_a_string()
# )

# Reasons for functions
# 1 - for organization - make it readable
# 2 - for reusability
# 3 - to avoid duplication or repetition of codes

def greet():    # greet is a function that takes in a string inside a variable and return a data
    say = "Hello"
    return say
  # parameters and arguments
greet()  # parameters is like a variable inside a function, that binds or hold the data. The data passed is called argument

def add_two_numbers(first_number, second_number): # what holds the argument which is in d function, is called a parameter
    return first_number + second_number
Output = add_two_numbers(8, 9)  # the value in here is called an argument
# print(
#     add_two_numbers(5,7),
#     add_two_numbers(6,7),
#     add_two_numbers(5,4),
#     add_two_numbers(3,8),
#     add_two_numbers(2,8),
#     add_two_numbers(15,17)
# )
adding_two_numbers()  #calling a function

# def adding_a_name_to_mailhost(name, host):
#     return name + host
# print(
#     adding_a_name_to_mailhost("sannimistura", "@gmail.com")
# )

def a_list_of_user_emails(host, list):
    user_mail_addresses = []
    for name in list:
        mail_address = name + host
        user_mail_addresses.append(mail_address)
    return user_mail_addresses
# print(
#     a_list_of_user_emails("@hotmail.com", ["mistura", "tomi", "ola", "arinze", "emmanuel","miracle"]),
#     a_list_of_user_emails("@gmail.com", ["mistura", "tomi", "ola", "arinze", "emmanuel","prince"])
# )

# Checking if the data meet certain condition

def registration_of_users(name, email, password):
    dict = {}
    if type(name) != str:
        return "Name is not a string"
    elif "@" not in email:
        return "Invalid email format."
    elif type(password) == str and len(password) < 5:
        return "Password must have more than 5 characters and must be a string"
    
    # Adding data to the dictionary
    dict["name"] = name
    dict["email"] = email
    dict["password"] = password
    return dict
# print(
#         registration_of_users("Mistura", "sanni@gmail.com", "12345")
#     )

def adding_user_to_list(user):
    list = []
    list.append(user)
    return list

output = adding_user_to_list(registration_of_users("Mistura", "sanni@gmail.com", "12345"))
print(output)


def multiply_function(itr, multiplier):
    list = []
    for num in itr:
        multiplied = num * multiplier
        list.append(multiplied)
    return list
# print(
#     multiply_function([2,4,6,8,10], 2)
#         )

# type of parameters

# positional arguments
def pos_func(pos1, pos2):
    return pos2, pos1
# print(
#     pos_func(2, 4)
# )

# keyword arguments   __ it doesn't respect position
def func1(posOne, posTwo):
    return posOne, posTwo
# print(
#     func1(posOne=3, posTwo=4)
# )

# default arguments
def game(action, level = 1):
    return action, level
# print(
#     game("start") or you can add a level of your choice in here
# )
    
# Variable arguments - ARGS   it returns a tuple and it takes only one asterisk
def func2(*params):
    return params
# print(
#     func2(1,2,3,4,5,6)
# )

# Keyword as an argument - KWARGS   it returns a dictionary and it takes two asterisks
def func3(**params):
    return params
# print(
#     func3(name="Mistura", age=27, email="sanni@gmail.com", password="12345")
# )

# Lambda functions - It is a light-weight function
# All the types of argument stated below are also used in lambda
say_hello = lambda: "Hello"
simple_arithmetics = lambda: 1 + 4
write_something = lambda: input("How are you today?: ")
condition_func = lambda status: "Yes" if status == "Present" else "No" 
# print(
#     # say_hello()
#     # simple_arithmetics()
#     # write_something()
#     condition_func("absent")
# )

# The HOF that just returns a function
def sentence(str):   # This is a function nesting
    def output():
        return str
    return output()
print(
    sentence("Don't give up! You are almost there!")
)

# The HOF that takes a function as an argument
def concat(param1, param2):
    return param1 + param2

def func(join):
    return join("sanni", "@gmail.com")
# print(
#     func(concat)
#     return join
# )
#     #    OR
# print(
#     func(concat("sanni", "@gmail.com"))
#  )


# Map, filter and reduce   - returns back a new list
# def map_func(params):
#     print(params)
#     return params
# map = list(map(map_func, [1,2,3,4,5,6,7]))
# print(map)

# def map_func(params):
#     calc = params * 3
#     return calc
# map = list(map(map_func, [1,2,3,4,5,6,7]))
# print(map)
# map = list(map(lambda params: params * 2, [1,2,3,4,5,6,7]))
# print(map)
remainders = list(filter(lambda params: params % 2, [1,2,3,4,5,6,7]))
print(remainders)
no_remainders = list(filter(lambda params: params % 2 == 0, [1,2,3,4,5,6,7]))
print(no_remainders)

# Reduce 
# def reduce_processor(result, item_in_list):
#     print(result, item_in_list)
#     return result + item_in_list
# reduce_func = reduce(reduce_processor,("The", "Quick","Brown","fox","jumps","over","the","lazy","dog",))
# print(reduce_func)

# checking for the longest word in the list
def reduce_processor(result, item_in_list):
   if len(result) > len(item_in_list):
    return result
   else: return item_in_list
reduce_func = reduce(reduce_processor,("The", "Quick","Brownies","fox","jumps","over","the","lazy","dog",))
print(reduce_func)

# Recursion - fibonacci sequence
def func5(num):
    num+= 5
    print(num)
    return func5(num)
func5(4)

