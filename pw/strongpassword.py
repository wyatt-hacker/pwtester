import re
import pyperclip

class checkStrongPassword():
 
    def __init__(self):
        #
        self.pattern_special_characters = re.compile(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]')
        self.pattern_capital_letters = re.compile(r'[A-Z]')
        self.pattern_repeating_numbers = re.compile(r'(\d)\1{2,}')
        self.common_words = ['password', 'admin', 'qwerty', 'letmein', 'welcome', 
                'monkey', 'dragon', 'master', 'hello', 'freedom',
                'whatever', 'computer', 'internet', 'sunshine']
        self.validated_password = None

    def getPassword(self):
        #if password empty, convert input to str
        password = input("Enter Password Here ")
        if password is None:
            print('You must enter a password!? Duh')

        if not isinstance(password, str):
            try:
                password = str(password)
            except (UnicodeEncodeError, TypeError):
                return("You tryna hack me? Do it again with normal characters!")
        else:
             return password 
 
    def validate_password(self,password,min_length=3):
        errors = []
        if len(password) < 16:
            errors.append("Password not long enough try to reach 16 characters")
            
        if  not self.pattern_capital_letters.search(password):
            errors.append("Include atleast one Capital Letter")

            
        if self.pattern_repeating_numbers.search(password):
            errors.append("Remove the repeating numbers from your password")

            
        if not self.pattern_special_characters.search(password):
            errors.append("Include atleast one special character")

            
        i = 0 
        while i < len(password) - (min_length - 1):
            # Find biggest slice starting at i
            max_possible_length = min(10, len(password) - i) 

            for seq_length in range(min_length, max_possible_length + 1):
                current_slice = password[i:i + seq_length] 

                if not current_slice.isdigit():
                    continue
                # At this point if a slice exists is shoud be identified, then we test for 
                # sequential numbers
                    is_ascending = True
                    for j in range(seq_length - 1):
                        if int(current_slice[j+1]) != int(current_slice[j]) + 1:
                            errors.append("Remove sequential numbers ie 123 456 789")
                            is_ascending = False
                            break
                    is_descending = True
                    for j in range(seq_length - 1):
                        if int(current_slice[j+1]) != int(current_slice) - 1:
                            errors.append("Remove sequential numbers ie 321 654 987")
                            is_descending = False
                            break
                
                if is_ascending or is_descending:
                    errors.append("Remove sequential numbers 123, 321, ie")
                    break
                i += 1
    
            if errors:
                print("Errors Found")
                for error in errors:
                    print(f" - {error}")
                return None
            else:
                print("Password is secure")
                self.validated_password = password
                return password

    def savetoClipboard(self):
        if self.validated_password:
            pyperclip.copy(self.validated_password)
            print("Password saved to Clipboard")


                