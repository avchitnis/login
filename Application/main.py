from login import Login
import os

options = input('Please select an option:\n[1️] Access account\n[2️] Create account\n[3] Delete account\nIndex: ')

os.system('cls' if os.name == 'nt' else 'clear')
username = input('Enter a valid username: ')
password = input('Enter a valid password: ')

os.system('cls' if os.name == 'nt' else 'clear')
print(Login(Login.input_validation(username, password)[0], Login.input_validation(username, password)[1]).choice(options))