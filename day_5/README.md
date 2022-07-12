#  Final Project - Email/Password checker/saver

A basic email and password checker program to check access credentials.

# Schedule

Starts at 9h30 and should end at 17h with +1 hour of tolerance (18h)

# Description

As a user I want to run a program/script where I pass an email string and a password string and the script validates if the email is valid and if the password is safe based on the following security rules:

* Password must have at least 8 characters and maximum 20 characters
* Password must have letters and numbers
* Password must have at least one capital letter
* Password cannot have the email name on the password string.
* Email must end with a @email.com substring
* Password cannot have 'password' string

Examples:

This will fail because password is bigger than 20 chars
```
email: bender.rodriguez@gmail.com
password: bitemyshinnyMETALass42
```

This will pass
```
email: theknights@montypython.com
password: NIIiiii666
```

Have fun :)

# Requirements
1. Use ```argparse``` python module to create the script input arguments
2. Store email and password on a file
3. The code must run inside a virtual environment
4. Checks if the email is a valid string email
5. Checks if the password follows the defined security rules
6. Gives error messages and must have exception handling.
7. Shows status messages using the ```logging``` module
8. Functions must have type hints and docstrings explaining what they do
9. Script must have unit tests and test the basic code functionality
10. Use ```pylint``` to lint your code to check if it follows a style guide
11. Create a branch on gitlab PyCademy repository and push your code. We will evaluate and classify each solution.
