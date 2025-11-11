import re
"""Im thinking i want to break apart the regex into the seperate checkers just for better readability
| 16 character min, no simple passwords, includes number, special character, 
 I also want a strong password to be saved to the clipboard | pyperclip
 Finding a library for graphical ui would be useful | tkinter
 I want to put in secure coding practices for cleaning the input
 """

class checkStrongPassword(input):
    # Make regex for strong password
    #Grab input and compare against
    # Return input on if 
    def __init__(self):
        #
        self.strongpw_regex = re.compile(r'''
        ^                   # Start of string anchor
        (?=.*[a-z])        # Positive lookahead - must contain at least one lowercase letter
        (?=.*[A-Z])        # Positive lookahead - must contain at least one uppercase letter
        (?=.*\d)           # Positive lookahead - must contain at least one digit
        (?=.*[@$!%*?&])    # Positive lookahead - must contain at least one special character
        [A-Za-z\d@$!%*?&]  # Allowed character set: letters, numbers, and specified special chars
        {16}               # Exactly 16 characters (no more, no less)
        $                  # End of string anchor
        ''', re.VERBOSE)
        

    def sanitizePassword(input):
        #if password empty, convert input to str
        if input is None:
            print('You must enter a password!? Duh')

        if not isinstance(input, str):
            try:
                password_input = str(input)
            except (UnicodeEncodeError, TypeError):
                return("You tryna hack me? Do it again with normal characters!")
    def checkPassword(input):
        password_obj = self.strongpw_regex.search(password_input)
        if password_obj.group() == False:
            print("password is weak sauce")
        i    