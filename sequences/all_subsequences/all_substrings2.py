
"""
all_substrings2.py
Function and program to find all the substrings of a given string.
Author: Vasudev Ram
Copyright 2018 Vasudev Ram
Web site: https://vasudevram.github.io
Blog: https://jugad2.blogspot.com
Twitter: https://mobile.twitter.com/vasudevram
Product store: https://gumroad.com/vasudevram
"""

from __future__ import print_function
import sys
from error_exit import error_exit
from debug1 import debug1

def usage():
    message_lines = [\
        "Usage: python {} a_string".format(sa[0]),
        "Print all substrings of a_string.",
        "",
    ]
    sys.stderr.write("\n".join(message_lines))

def all_substrings2(s):
    """
    Generator function that yields all the substrings 
    of a given string.
    Algorithm used:
    1. len_s = len(s)
    2. if len_s == 0, return ""
    3. (else len_s is > 0):
       for substr_len in 1 to len_s:
           find all substrings of s that are of length substr_len
           yield each such substring 
    Expected output for some strings:
    For "a":
        "a"
    For "ab":
        "a"
        "b"
        "ab"
    For "abc:
        "a"
        "b"
        "c"
        "ab"
        "bc"
        "abc"
    For "abcd:
        "a"
        "b"
        "c"
        "d"
        "ab"
        "bc"
        "cd"
        "abc"
        "bcd"
        "abcd"
    """

    len_s = len(s)
    substr_len = 1
    while substr_len <= len_s:
        start = 0
        end = start + substr_len
        while end <= len_s:
            debug1("s[{}:{}] = {}".format(\
                start, end, s[start:end]))
            yield s[start:end]
            start += 1
            end = start + substr_len
        substr_len += 1

def main():
    if lsa != 2:
        usage()
        error_exit("\nError: Exactly one argument must be given.\n")

    if sa[1] == "":
        print("")
        sys.exit(0)

    for substring in all_substrings2(sa[1]):
        print(substring)

sa = sys.argv
lsa = len(sa)

if __name__ == "__main__":
    main()

