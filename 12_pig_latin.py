"""
Pig Latin is a game of alterations played on the English language game. A simplified version of pig latin uses
the following algorithm:

if the word begins with a vowel (a, e, i, o , u), add "ay" to the end of the word (apple becomes appleay)
if the word begins with a consonant, move the first letter to the end and then add "ay" (bat becomes atbay)

for example: hello how are you = ellohay owhay areay ouyay

1. write code to convert a single word
2. write code to convert the sentence "hello how are you"
"""

# Pig Latin


sentence = "Hello how are you"
word_list = sentence.split(" ")
total_words = len(word_list)
new_sentence = ""

for i in range(total_words):
    current_word = word_list[i]
    first_letter = current_word[0].lower()
    if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
        # must be a vowel
        new_word = current_word + "ay"
        new_sentence = new_sentence + " " + new_word
    else:
        # must be a consonant
        new_word = current_word[1:]
        new_word = new_word + first_letter + "ay"
        new_sentence = new_sentence + " " + new_word
    # end if
# end for

# the first letter will always be a space so remove it!
new_sentence = new_sentence[1:]
print(new_sentence)



