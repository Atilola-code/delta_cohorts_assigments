# vowels = "aeiou"
# length = len(vowels)
# # print(length)    gives the length of a string
# reverse_vowel = vowels[::-1]
# print(reverse_vowel) # reverses a string

firstName = "Mistura"
lastName = "Sanni"


sentence = "I need the name of Sarah Adams to be joined to sarahadams@gmail.com"
output = sentence.replace("Sarah", firstName).replace("Adams", lastName).replace("sarahadams", firstName.lower() + lastName.lower())
# print(output)

length_of_space = sentence.count(" ")
print(length_of_space)

# Another method

num = 0
for char in sentence:
    if char == " ":
        num += 1
    else:
        print(num)

print(sentence.count(" "))


# max_word = ""
# for word in sentence.split():
#     if len(word) > len(max_word):
#         max_word = word

# # print("The longest word in the string is", max_word)


# fruits = ["apple", "banana", "carrot", "kiwi"]
# highest_fruit = ""
# for fruit in fruits:
#     if len(highest_fruit) < len(fruit):
#         highest_fruit = fruit

# else:
#     print(highest_fruit)











