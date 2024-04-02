password = input("Please enter a password that is at least 8 characters: ")

if (len(password) <= 8):
    print(password + " is an invalid password")
else:
    print(password + " is a valid password")
