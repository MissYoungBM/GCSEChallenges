"""
Checks if the string entered by the user is a palindrome. A palindrome is a word that reads the same forwards as it does
backwards like “racecar”.
"""

word = input("Enter a word to check if it is a palindrome: ")
# word = "racecar1"

# reverse the word
word_len = len(word)
reversed_word = ""
for i in range(word_len):
    reversed_word = word[i] + reversed_word
#next i

# check the reversed word against the word. If same, it must be a palindrome.
if reversed_word == word:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
#end if

# In advanced coding, can write the above 4 lines, in one using the ternary "operator":
# print("The word is" + ("" if word == reversed_word else " not") + " a palindrome")


# def reverse(word):
#     """
#     This is how you could do it in Edexcel GCSE using the given standard python code in the spec.
#     Its no less code, but I think it is easier to read.
#     """
#
#     reversed_word = ""
#     for c in word:
#         reversed_word = c + reversed_word
#     # next c
#     return reversed_word
# #end def
#
# reverse("racecar")
