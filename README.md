# Brief overview
- A login system consisting of input sanitation, input validation on a user's username and password

# Details

<h2>
  main.py
</h2>

- Takes two inputs from the user, a username and a password
- Provides these to the `Login` class within `login.py`

<h2>
  login.py
</h2>

<h4>
  Recieving input
</h4>

- The user's username and password are recieved from `main.py`
- This input is sanitised and validated
- The user is then asked to select one of the following options:
  - creating an account
  - accessing an existing account
  - deleting an account

<h4>
  Execution
</h4>

- The password is hashed with a salt and stored within `accounts.json`
  - This ensures the safety of passwords as they are encrypted
- According to the user's choice, a corresponding subroutine is called

<h2>
  other
</h2>

- `accounts.json` is where all the accounts are stored
- Error classes are stored within `exceptions.py`

# Reflection
- This project has refined my use of the JSON module in python
