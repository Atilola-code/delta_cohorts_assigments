from functools import reduce

# Number 1

def update_name(full_name, changed_name):
    full_name = "Chuka Emeka"
    changed_name = full_name.replace("Chuka Okeke")
    return full_name, changed_name
print(
    update_name()
)


# Number 2
def bio_data(height, age):
    return f"My height is: {height} and my age is: {age}"
print(
    bio_data(1.78, 28)
)

# Number 3
def check_login_status(is_logged_in= True):
    return type(is_logged_in)
print(
    check_login_status()
)

# Number 4
def full_name(first, last):
    return f"{first} {last}"
print(
    full_name("Mistura", "Sanni")
)

# Number 5
def get_remainder(a, b):
    if b == 0:
        return "Cannot be divided by zero"
    return a % b
print(
    get_remainder(9,4)
)

# Number 6
def add_floats(a, b):
    return float(a + b)
print(
    add_floats(5.8, 2.5)
)

#       OR

# def add_floats(a, b):
#     return (a + b)
# print(
#     add_floats(8.8, 2.5)
# )

# Number 7
def compare_numbers(a, b):
    if a >= b:
        return True
    else:
        return False
print(
    compare_numbers(5,2),
    compare_numbers(4,8)
)

#       OR

# def compare_numbers(a, b):
#    return a >= b
# print(
#     compare_numbers(8,2),
#     compare_numbers(2,9)
# )

# Number 8
def access_granted(has_id, has_clearance):
    return has_id and has_clearance
print(
    access_granted(True,True),
    # access_granted(True,False),
    # access_granted(False,True)
)

# Number 9
def can_enter(has_pass, knows_manager):
    return has_pass and knows_manager
print(
    can_enter(True,True),
    # can_enter(True,False),
    # can_enter(False,True)
)

# Number 10
def reverse_access(can_enter):
    return not can_enter
print(
    reverse_access(True),
    # reverse_access(False)
    )

# Number 11

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
print(
    reverse_sentence("The boy is gone"),
    # reverse_sentence("Today is a beautiful day")
)

# Number 12
get_odds = list(filter(lambda numbers: numbers % 2 != 0, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))
print(get_odds)

# Number 13
def total_word_count(*sentences):
    total_words = 0
    for sentence in sentences:
        word = sentence.split()
        total_words += len(word)
    return total_words
print(
        total_word_count("The goal is to keep pushing and never give up because there is a light at the end of every tunnel")
    )

# Number 14
def product_of_list(numbers):
    def multiply(num1, num2):
        return num1 * num2
    return reduce(multiply, numbers)
print(
    product_of_list([1,2,3,4,5,6,7,8,9])
    # product_of_list([1,2,3,4,5,6])
)

# Number 15
def censor_vowels(word):
    vowel = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter in vowel:
            result += "*"
        else:
            result += letter
    return result
print(
    # censor_vowels("NaijaTech"),
    # censor_vowels("Defibrillator")
    censor_vowels("Aeronautic")
)



