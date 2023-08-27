"""
1. Create a function which will convert a given decimal up to 255 into its 8-bit binary equivalent.
2. Create a function which will convert a given 8-bit binary number to decimal.
"""

def convert_d_to_b(number, total_bits=8):
    """
    The problem statement require the max number to be 255 or 8 bits
    so can make some assumptions to simplify.
    Return as string to ensure it displays as binary

    :return: the binary number as a string
    """
    binary_string = ""
    current_ph = 2**(total_bits - 1)
    for i in range(total_bits):
        if number / current_ph >= 1:
            binary_string += "1"
            number -= current_ph
        else:
            binary_string += "0"
        #end if
        current_ph = current_ph / 2
    #next i

    return binary_string
#end def

def convert_b_to_d(number):
    """
    The problem statement require an *8 bit* number
    so can make some assumptions to simplify
    Input is a string of 8-bit binary numbers
    :return: the denary number
    """
    total_bits = len(number)
    current_ph = 2**(total_bits - 1)
    denary = 0
    for i in range(total_bits):
        current_digit = number[i]
        if current_digit == "1":
            denary += current_ph
        #end if
        current_ph = current_ph / 2
    #next i

    return int(denary)
#end def

print(convert_d_to_b(15, 8))
print(convert_b_to_d("00011111"))