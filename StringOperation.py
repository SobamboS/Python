# s = "olusola sobambo"
# print(s.upper())  # will make it capital letter
# print(s.lower())  # will make it small letter
# print(s.title())  # will capitalize the title
# print(s.capitalize())  # will capitalize the first letter
# print(s.swapcase())   # will capitalize everything
# print(s.casefold())  # will make it small letter
# print(s.startswith('o'))
# print(s.startswith('O'))
# print(s.endswith('sobambo'))
# print(s.rjust(20))
# print(s.rjust(10))
# print(s.ljust(70))
# print(s.center(50))
# print(s.center(50, '#'))
#
# for i in range(1, 55):
#     print('*' * i)
#
# for i in range(1, 10):
#     print(('*' * i).rjust(10))
#
# for i in range(1, 10):
#     print(('*' * i).center(10))
#
# for i in range(1, 10, 2):  # print in range
#     print(('*' * i).center(10))
#
# print(s.count('b'))
# print(s.count('o'))
# print(s.find('s'))
# print(s.find('a', 2))
# print(s.find('b', 2, 5))
# print(s.index('b'))
# print(s.index('a', 3))
# print(s.r index('o',))
# print(s.replace('s', '$'))  # to replace a letter in a string


# encoding words
import string
word = input("What would you like to encode ")
key = int(input("Your key ? "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_letters_code = upper_letters[key:] + upper_letters[:key]

letters = lower_letters + upper_letters
letters_code = lower_letters_code + upper_letters_code

print(letters)
print(letters_code)

encoded_word = word.translate(str.maketrans(letters, letters_code))
print(word)
print(encoded_word)

# decoding words

decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))
print(decoded_word)

print("Now, the brute force approach")
for i in range(1, 27):
    lower_letters_code = lower_letters[i:] + lower_letters[:i]
    upper_letters_code = upper_letters[i:] + upper_letters[:i]

    letters = lower_letters + upper_letters
    letters_code = lower_letters_code + upper_letters_code

    print(encoded_word.translate(str.maketrans(letters_code, letters)))