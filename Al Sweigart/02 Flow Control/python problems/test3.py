# Ask the user for a username and password
# Allow only 3 attempts
# If the credentials are correct, print a success message and exit
# if the user fails 3 times, lock them out.

# GO!!

userName = "Maple"
userPassWord = "W@ndaVision19"
print("Welcome, Please Login..")

entry = 0
while entry < 3:
    ask1 = input("Username: ")
    ask2 = input("Password: ")

    entry += 1
    if ask1 == userName and ask2 == userPassWord:
        print(f"Welcome, {ask1}!")
        break

    elif ask1 == userName and ask2 != userPassWord:
        print(f"Invalid Password, {entry} attempt(s), {3 - entry} entries left")
    elif ask1 != userName and ask2 == userPassWord:
        print(f"Invalid Username, {entry} attempt(s), {3 - entry} entries left")
    elif ask1 != userName and ask2 != userPassWord:
        print(f"Invalid Username and Password! {entry} attempt(s), {3 - entry} entries left")
else:
    print("Out of attempts")
