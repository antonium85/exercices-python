#My Login Script - www.101computing.net/my-login-script

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

def signIn(max_attempt):
    attempt = 0
    while attempt < max_attempt:
        attempt += 1
        username = input("Username?")
        password = input("Password?")
        if password in d.keys() and d[password] == username :
            print("You are logged in !")
            return True
        else:
            print("Wrong username or password! Try again !")

    return False

def signUp():
    first_name = input("First Name ? ")
    last_name = input("Last Name ? ")

    username = first_name[0].lower() + last_name.lower()
    i = 0
    while username in d.values():
        i += 1
        if i > 0 : username = f'{username[:len(username)]}{i}'

    print("Your username : " + username)
    password = input("Password : ")

    file = open("usernames.txt","a")
    file.writelines("\n" + username.lower() + "," + password + ",\n")
    file.close()

new_user = input("New User (0) or Existing User (1) : ")

if new_user == "0":
    signUp()
else:
    if not signIn(MAX_ATTEMPT):
        print("Try again later ! ")

#if not signIn(MAX_ATTEMPT):
#    print("Try again later !")