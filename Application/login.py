from exceptions import *
import hashlib
import json
import uuid
import os

class Login():
    def __init__(self, username: str, password) -> None:
        self.username = username
        self.password = password

    @staticmethod   
    def get_users():
        with open('Application/accounts.json', 'r+') as f:
            return json.load(f)

    def access_account(self):
        data = Login.get_users()

        for user in data['users']:
            if self.username == user['username']:
                if hashlib.sha512(self.password + user['salt'].encode('utf-8')).hexdigest() == user['hash']:
                    return f'Successfully logged in as {self.username}.'

                else:
                    raise PasswordError

        raise UsernameError
    
    def create_account(self):
        data = Login.get_users()
            
        if self.username not in [user['username'] for user in data['users']]:
            salt = str(uuid.uuid4()).encode('utf-8')
            hash = hashlib.sha512(self.password + salt).hexdigest()
            with open('Application/accounts.json', 'w') as f:
                data['users'].append({'username': self.username, 'hash': hash, 'salt': salt.decode('utf-8')})
                json.dump(data, f, sort_keys = True, indent = 4)
            
            return f'Successfully created account: \'{self.username}\'.'
        
        else:
            raise UsernameError
    
    def delete_account(self):
        data = Login.get_users()

        for user in data['users']:
            if self.username == user['username']:
                if hashlib.sha512(self.password + user['salt'].encode('utf-8')).hexdigest() == user['hash']:
                    with open('Application/accounts.json', 'w') as f:
                        del data['users'][data['users'].index(user)]
                        json.dump(data, f, sort_keys = True, indent = 4)

                    return f'Successfully deleted account: \'{self.username}\'.'
            
                else:
                    raise PasswordError
        
        raise UsernameError
        
    @staticmethod
    def input_validation(username, password):
        valid = False
        while not valid:
            os.system('cls' if os.name == 'nt' else 'clear')

            try:
                if not username.isalnum():
                    raise UsernameError.UsernameTypeError        

                elif len(password) < 8:
                    raise PasswordError.PasswordLengthError
                    
                elif password == password.lower():
                    raise PasswordError.PasswordUppercaseError

            except UsernameError.UsernameTypeError:
                print('Username must be alphanumeric')
                
            except PasswordError.PasswordLengthError:
                print('Password must be over 8 characters')

            except PasswordError.PasswordUppercaseError:
                print('Password must have an uppercase letter')
            
            else:
                valid = True

            finally:
                if not valid:
                    username = input('Enter a valid username: ')
                    password = input('Enter a valid password: ')

        return username, password

    def choice(self, option):
        match option:
            case '1':
                try:
                    return Login(self.username, self.password.encode('utf-8')).access_account()

                except UsernameError:
                    return f'No existing user with username: \'{self.username}\' was found.'

                except PasswordError:
                    return f'Incorrect password for \'{self.username}\' entered.'

            case '2':
                try:
                    return Login(self.username, self.password.encode('utf-8')).create_account()
                
                except UsernameError:
                    return f'Existing account with username: \'{self.username}\' was found.'

            case '3':
                try:
                    return Login(self.username, self.password.encode('utf-8')).delete_account()

                except UsernameError:
                    return f'No existing account with username: \'{self.username}\' was found.'

                except PasswordError:
                    return f'Incorrect password for \'{self.username}\' entered.'
                
            case _:
                return f'Invalid option entered'