#! python3

import re

password = input(' Password: ')

def is_password_strong(password):
 
    
    length_regex = re.compile(r'.{8,}')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    
    length = length_regex.search(password) is not None
    case = (uppercase_regex.search(password) is not None and
        lowercase_regex.search(password) is not None)
    digit = digit_regex.search(password) is not None

    print(length and case and digit)
    
is_password_stong(password)
