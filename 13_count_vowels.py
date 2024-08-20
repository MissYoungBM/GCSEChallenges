"""
1. Enter a string and the program counts the number of vowels in the text.
2. Report a sum of each vowel found.
"""

sentence = "Computer Science is great"
total_vowels = 0
sentence_len = len(sentence)
for i in range(sentence_len):  # could use char in sentence but trying to use first principles
    lower_char = sentence[i].lower()
    # could use "if lower_char in vowels" but trying to use first principles
    if lower_char == "a" or lower_char == "e" or lower_char == "i" or lower_char == "o" or lower_char == "u":
        total_vowels = total_vowels + 1
    #end if
#next i
# print(total_vowels)


# extension
vowels = ["a", "e", "i", "o", "u"]
vowel_counts = [0, 0, 0, 0, 0]
total_vowels = 0
for i in range(len(sentence)):  # could use char in sentence but trying to use first principles
    lower_char = sentence[i].lower()
    # could use "if lower_char in vowels" but trying to use first principles
    if lower_char == "a" or lower_char == "e" or lower_char == "i" or lower_char == "o" or lower_char == "u":
        total_vowels = total_vowels + 1
        # there are other ways to do this with built-in libraries,
        # but this is pure first principles
        if lower_char == "a":
            vowel_counts[0] += 1
        elif lower_char == "e":
            vowel_counts[1] += 1
        elif lower_char == "i":
            vowel_counts[2] += 1
        elif lower_char == "o":
            vowel_counts[3] += 1
        else:
            vowel_counts[4] += 1
        #end if
    #end if
#next i

print("There are " + str(total_vowels) + " vowels")
for i in range(len(vowels)):
    print("There are " + str(vowel_counts[i]) + " " + vowels[i])
#next i