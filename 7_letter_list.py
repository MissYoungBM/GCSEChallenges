"""
Write a program that lets a user choose a letter. The program will then find all the words beginning with that letter in
a list and print them out. It should also say how many words it found
"""

from support_files.words import word_list
#word list will contain an array (list) of words

first_letter = input("Enter a letter to search for words beginning with that letter: ")
total_words = 0
num_items = len(word_list)
for i in range(num_items):
    current_word = word_list[i]
    if current_word[0] == first_letter:
        print(current_word)
        total_words += 1
    #end if
#next i

print("The total words beginning with " + first_letter + " was " + str(total_words))
