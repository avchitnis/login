#Exceptions catagorised into 3 classes: username, password and option
class UsernameError(Exception):
    """Raise exception for invalid username"""
    
    class UsernameTypeError(Exception):
        """Raise exception if username is not alphanumeric"""

class PasswordError(Exception):
    """Raise exception for invalid password"""

    class PasswordLengthError(Exception):
        """Raise exception for too short of a password"""

    class PasswordUppercaseError(Exception):
        """Raise exception for no uppercase letter in password"""

class OptionError(Exception):
    """Raise exception for invalid option"""