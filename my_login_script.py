#My Login Script - www.101computing.net/my-login-script

import string

USERNAME="admin"
PASSWORD="p4$$W0rd"
MAX_ATTEMPT = 3

print("#####################")
print("#    Login Screen   #")
print("#####################")

#Opening the text file in read mode
#file = open("usernames.txt","r")

#Complete the login script from here
#print(file.read())
d = dict()
with open("usernames.txt","r") as file:
    for line in file:
        str = line[:len(line)-2]
        username, password = str.split(",")
        d[password] = username
print(d)

#Closing thte text file
file.close()

def sign_in(max_attempt):
    attempt = 0
    while attempt < max_attempt:
        attempt += 1
        username = input("Username ? ")
        password = input("Password ? ")
        if password in d.keys() and d[password] == username :
            print("You are logged in !")
            return username
        else:
            print("Wrong username or password! Try again !")

    return None

"""
The password has to be at least 8 characters long,
The password has to include uppercase letters and lowercase letters,
The password has to letters and numbers,
The password has to include at least one punctuation sign.
"""
def is_strong_password(password):
    has_punctuation_sign = False
    for i in password:
        if i in string.punctuation : 
            has_punctuation_sign = True
            break
    return has_punctuation_sign and not password.islower() and not password.isdigit() and not len(password) < 8

def changePassword(username):
    old_password = ""
    for key, value in d.items():
        if username == value:
            old_password = key
            break

    new_password = "0"
    confirm_password = "1"
    strong_password = False

    while not (new_password == confirm_password) or not strong_password:
        new_password = input("New password ? ")
        confirm_password = input("Confirm password ? ")
        strong_password = is_strong_password(new_password)

        if new_password == confirm_password and strong_password :
            d[new_password] = d.pop(old_password)
            break

    file = open("usernames.txt","w")
    for key, value in d.items():
        file.writelines(value + "," + key + ",\n")
    file.close()

def sign_up():
    first_name = input("First Name ? ")
    last_name = input("Last Name ? ")

    username = first_name[0].lower() + last_name.lower()
    i = 0
    while username in d.values():
        i += 1
        if i > 0 : username = f'{username[:len(username)]}{i}'

    print("Your username : " + username)
    password = input("Password : ")
    while not is_strong_password(password):
        password = input("Password : ")

    file = open("usernames.txt","a")
    file.writelines(username.lower() + "," + password + ",\n")
    file.close()

new_user = input("New User (0) or Existing User (1) : ")

if new_user == "0":
    sign_up()
else:
    username = sign_in(MAX_ATTEMPT)
    if username == None:
        print("Try again later ! ")
    else:
        print("Change password now ")
        changePassword(username)

#if not sign_in(MAX_ATTEMPT):
#    print("Try again later !")