"""
Only accept a new password if it is:
1. At least eight characters long
2. Has lower case and upper case letters.

The password reset program should also make the user inputs their new password twice so that the computer knows that the
user has not made any mistakes when typing their new password.
"""

# password = input("Enter a new password: ")
password = "123456aZ"

has_upper = False
has_lower = False

password_len = len(password)
for i in range(password_len):
    current_char = password[i]
    if current_char >= "a" and current_char <= "z":
        has_lower = True
    #end if
    if current_char >= "A" and current_char <= "Z":
        has_upper = True
    #end if
#next i

if password_len >= 8 and has_lower and has_upper:
    print("Valid password")
    password_check = input("now enter it again for validation: ")
    if password_check == password:
        print("Passwords match, password successfully updated")
    else:
        print("Your passwords don't match, password not updated")
    #end if
else:
    print("Invalid password")
#end if


