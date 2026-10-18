# Password checker (password_check.py): ask for a password. Print Strong if it has at least 8 characters and contains a digit, otherwise print Weak.
# Hint: use len() and loop over the characters with isdigit().
password = input("Enter a password: ")
if len(password) >= 8 :
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        print("Strong")
else:
    print("Weak")