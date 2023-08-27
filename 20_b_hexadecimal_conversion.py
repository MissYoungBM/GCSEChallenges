"""
1. Create a function which will convert a given decimal up to 255 into its hexadecimal equivalent.
2. Create a function which will convert a given 2-digit hexadecimal number to decimal.
3. Create a function which will convert a given 2-digit hexadecimal number to 8-bit binary number.
4. Create a function which will convert an 8-bit binary number to a 2-digit hexadecimal number.
"""

hex_lookup = ["0","1","2","3","4","5","6","7","8","9","A", "B", "C", "D", "E", "F"]

def convert_d_to_h(number, total_bits=2):
    """
    The problem statement require the max number to be 255 or 8 bits
    so can make some assumptions to simplify.
    Return as string to ensure it displays as binary

    :return: the binary number as a string
    """
    hex_string = ""
    current_ph = 16**(total_bits-1)
    for i in range(total_bits):
        if number / current_ph >= 1:
            value = int(number // current_ph)
            hex_string += hex_lookup[value]
            number = number - (value * current_ph)
        else:
            hex_string += "0"
        #end if
        current_ph = int(current_ph / 16)
    #next i

    return hex_string
#end def

def convert_h_to_d(number):
    """
    The problem statement require the max number to be 255 or 8 bits
    so can make some assumptions to simplify.
    Return as string to ensure it displays as binary

    :return: the binary number as a string
    """
    total_bits = len(number)
    denary = 0
    current_ph = 16**(total_bits-1)
    for i in range(total_bits):
        current_digit = number[i]
        if current_digit.upper() == "A" or current_digit == "B" or current_digit == "C" or current_digit == "D" or current_digit == "E" or current_digit == "F":
            digit_value = ord(current_digit) - 55  # (65 is A and we are counting from 10)
        else:
            digit_value = int(current_digit)
        #end if
        denary += (current_ph * digit_value)
        current_ph = int(current_ph / 16)
    #next i

    return denary
#end def

#print(convert_d_to_h(42))
print(convert_h_to_d("10"))