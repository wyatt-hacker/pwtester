import re
import tkinter
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
        self.pattern_special_characters = re.compile(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]')
        self.pattern_capital_letters = re.compile(r'[A-Z]')
        self.pattern_repeating_numbers = re.compile(r'(\d)\1{2,}')
        self.common_words = ['password', 'admin', 'qwerty', 'letmein', 'welcome', 
                'monkey', 'dragon', 'master', 'hello', 'freedom',
                'whatever', 'computer', 'internet', 'sunshine']

    def sanitizePassword(input):
        #if password empty, convert input to str
        if input is None:
            print('You must enter a password!? Duh')

        if not isinstance(input, str):
            try:
                password_input = str(input)
            except (UnicodeEncodeError, TypeError):
                return("You tryna hack me? Do it again with normal characters!")
 
    def check_length(input):
        if len(input) >= 16:
            continue
        else:
            print("Password not long enough reach 16 characters")

    def find_all_sequential_numbers(input, min_length=3):
        """
        Find all sequential numbers and return red x if anyfound
        """
        sequences_found = [] # Do non empty list return True?

        i = 0 
        while i < len(input) - (min_length - 1):
            # Find biggest slice starting at i
            max_possible_length = min(10, len(input) - i) 

            for seq_length in range(min_lenght, max_possible_length + 1):
                current_slice = password[i:i + seq_length] # I think we remove the 1 so wehen we have it follow an i theres no out of bounds issue

                if not current_slice.isdigit():
                    continue
                # At this point if a slice exists is shoud be identified, then we test for 
                # sequential numbers
                is_ascending = True
                for j in range(seq_len - 1):
                    if int(curent_slice[j+1]) != int(current_slice[j]) + 1:
                        is_ascending = False
                        break

                is_descending = False
                for j in range(seq_length - 1):
                    if int(current_slice[j+1]) != int(current_slice) - 1:
                        is_descending = False
                        break

            if is_ascending or is_descending:
                print("No sequential numbers allowed ie, 123 or 321")

        return True



                