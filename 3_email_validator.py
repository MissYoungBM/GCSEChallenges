"""
Make a program to check whether an email address is valid or not.

Make sure that there are no spaces, that there is *one* @ symbol and a dot somewhere after it.

"""


email = "me@me.com"

has_spaces = False
has_at = False
has_dot_after_at = False
email_len = len(email)

for i in range(email_len):
    if email[i] == " ":
        has_spaces = True
    #end if
    if email[i] == "@":
        has_at = True
    #end if
    if email[i] == "." and has_at:
        has_dot_after_at = True
    #end if
#next i

if not has_spaces and has_at and has_dot_after_at:
    print("Valid email")
else:
    print("invalid email")
#end if
