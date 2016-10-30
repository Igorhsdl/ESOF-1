#! python3

import re

string = input(" Strings: ")
bad_chars = input(" Characters: ")

def regex_strip(string, bad_chars):
    
    strip_regex = re.compile('[%s]' % bad_chars)
    return strip_regex.sub('', string)
    
try:
    print(regex_strip(string, bad_chars))
except TypeError:
    print(regex_strip(string, ' '))
