#My Login Script - www.101computing.net/my-login-script

from random import randint
import string

USERNAME="admin"
PASSWORD="p4$$W0rd"
MAX_ATTEMPT = 3

class Utils:
    @staticmethod
    def is_strong_password(password):
        #The password has to be at least 8 characters long,
        #The password has to include uppercase letters and lowercase letters,
        #The password has to letters and numbers,
        #The password has to include at least one punctuation sign.
        has_punctuation_sign = False
        for i in password:
            if i in string.punctuation : 
                has_punctuation_sign = True
                break
        return has_punctuation_sign and not password.islower() and not password.isdigit() and not len(password) < 8

    @staticmethod
    def get_dictionnary_key(dict, input):
        for key, value in dict.items():
            if input == value:
                return key

        return None
    
    @staticmethod
    def read_data_from_file(filename):
        d = dict()
        with open(filename,"r") as file:
            for line in file:
                str = line[:len(line)-2]
                username, password = str.split(",")
                d[password] = username
        file.close()
        return d

    @staticmethod
    def write_new_data_to_file(username, password, filename):
        file = open(filename,"a")
        file.writelines(username.lower() + "," + password + ",\n")
        file.close()

    @staticmethod
    def rewrite_data_file(dict, filename):
        file = open("usernames.txt","w")
        for key, value in dict.items():
            file.writelines(value + "," + key + ",\n")
        file.close()

    # The computer displays a random 3 digit number on the screen 
    # and asks the user to enter this number when login in.
    @staticmethod
    def simple_captcha():
        print("######   ARE YOU HUMAN ?   #####")
        checked = False
        count = 0

        while not checked and count < 3 :
            random_number = randint(100,999)
            n = input(f'What do you see ({random_number}) ? ')
            print(n)
            if (random_number == int(n)):
                checked = True
            else:
                print('Try again ! ')
                count += 1

        return checked

    #The computer displays a random arithmetic question such as “what is 7+3?”. 
    #The user has to answer this question correctly when login in.
    @staticmethod
    def advanced_captcha():
        print("######   ARE YOU HUMAN ?   #####")
        checked = False
        count = 0

        while not checked and count < 3 :
            random_x = randint(1,9)
            random_y = randint(1,9)
            n = input(f'What is {random_x} + {random_y} ? ')

            if (random_x + random_y == int(n)):
                checked = True
            else:
                print('Try again ! ')
                count += 1

        return checked

class LoginScript:
    def __init__(self):
        self.data = Utils.read_data_from_file("usernames.txt")
        self._username = ""

    def __del__(self):
        self.data.clear()
        print("#####    See you again   #####")

    def get_data(self):
        return self.data

    def is_logged_in(self):
        return self._username != ""

    def sign_up(self):
        first_name = input("First Name ? ")
        last_name = input("Last Name ? ")

        username = first_name[0].lower() + last_name.lower()
        check_username = username
        i = 0
        #print(self.data.values())
        while check_username in self.data.values():
            i += 1
            check_username = f'{username}{i}'
            print(check_username)
        username = check_username

        print("Your username : " + username)
        password = input("Password : ")
        while not Utils.is_strong_password(password):
            password = input("Password : ")

        Utils.write_new_data_to_file(username,password,"usernames.txt")

    def sign_in(self, max_attempt):
        attempt = 0
        while attempt < max_attempt:
            attempt += 1
            username = input("Username ? ")
            password = input("Password ? ")

            if Utils.simple_captcha() :
                if password in self.data.keys() and self.data[password] == username :
                    print("#####    You are logged in !     #####\n")
                    self._username = username
                    return True
                else:
                    print("Wrong username or password! Try again !")
            else:
                print("Are you robot ? Try again !")

        return False

    def changePassword(self):
        old_password = Utils.get_dictionnary_key(self.data,self._username)

        new_password = "0"
        confirm_password = "1"
        strong_password = False

        while not (new_password == confirm_password) or not strong_password:
            new_password = input("New password ? ")
            confirm_password = input("Confirm password ? ")
            strong_password = Utils.is_strong_password(new_password)

            if not new_password == confirm_password:
                print("Confirm password is not the same !!! ")
            else:
                if not strong_password :
                    print("Password is not strong enough !!! ")
                else:
                    self.data[new_password] = self.data.pop(old_password)
                    break
        Utils.rewrite_data_file(self.data,"usernames.txt")

print("##########################################################")
print("#                        Login Screen                    #")
print("##########################################################")
print("1 : Sign Up - 2 : Login - 3 : Change password - 4 : Logout\n") 

action = input("What do you want to do now ? ")

login = LoginScript()
#print(login.get_data())
while not action == "4" :
    if action == "1":
        login.sign_up()
    elif action == "2":
        if not login.sign_in(MAX_ATTEMPT) :
            print("Try again later ! ")
    elif action == "3":
        if login.is_logged_in():
            print("######   Change password now    ######")
            login.changePassword()
        else:
            print("#####    You need to log in first    #####")
    else:
        print("#####    Invalid action      #####")

    print("1 : Sign Up - 2 : Login - 3 : Change password - 4 : Logout\n")
    action = input("What do you want to do now ? ")
del login

#if not sign_in(MAX_ATTEMPT):
#    print("Try again later !")