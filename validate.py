import re
import datetime

class Validation():
    def is_numeric(self, val):
        val = str(val)
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  

    def is_alphabetic(self, val):
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_alphanumeric(self, val):
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False  

    def is_phone_number(self, val):
        val = str(val)
        if re.search(r'(^\d{2} \d{4} \d{4}))', val):
            print("Valid phone number")
            return True
        else:
            print("Invalid phone number")
            return False  

    def is_email(self, val):
        val = str(val)
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)+', val):
            print("Valid email")
            return True
        else:
            print("Invalid email")
            return False  

        
    def is_alphabetic_with_space(self, val):
        if re.search(r'(^[a-zA-Z]+(\s[a-zA-Z]+)?$)', val):
            print("alphabetic w/ space")
            return True
        else:
            print("Not alphabetic w/ space")
            return False

    def is_alphanumeric_with_space(self, val):
        if re.search(r'(\w+\s\w+)', val):
            print("Alphanumeric w/ space")
            return True
        else:
            print("Not alphanumeric w/ space")
            return False
   
    pass

if __name__ == '__main__':
    pass        