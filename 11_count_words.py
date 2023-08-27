"""
Counts the number of individual words in a string.
"""


# main challenge

def get_total_words(sentence):
    # so the easy way to do this is
    # total_words = len(sentence.split(" ")) !!!
    # but that is not very "GCSE Computer Science"
    # also see below for edge cases.

    total_words = 0
    sentence_len = len(sentence)
    for i in range(sentence_len):
        if sentence[i] == " ":
            total_words += 1
        # end if
    # next i

    # need to add 1 to total words as the last word does (should) not have a space after it.
    # a better program would account for this. Even the easy version has this fault
    # you might be able to fix that by using - total_words = len(sentence.strip().split(" "))
    # but if there is a space then "." or any other non character, it would not work.

    total_words += 1
    return total_words
# end def


sentence = "computer science is great"
num_words = get_total_words(sentence)

print("There are " + str(num_words) + " words in the sentence")
