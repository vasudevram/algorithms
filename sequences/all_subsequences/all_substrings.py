
"""
all_substrings.py
Function and program to find all the substrings of a given string.
Author: Vasudev Ram
Web site: https://vasudevram.github.io
Blog: https://jugad2.blogspot.com
Twitter: https://mobile.twitter.com/vasudevram
Product Store: https://gumroad.com/vasudevram
"""

from __future__ import print_function
import sys
from error_exit import error_exit
from debug1 import debug1

def usage():
    message_lines = [\
        "Usage: python {} a_string".format(sa[0]),
        "Print all substrings of a_string.",
    ]
    sys.stderr.write("\n".join(message_lines))

def all_substrings(s):
    """
    Generator function that yields all the substrings of a given string.
    """

    ls = len(s)
    if ls == 0:
        usage()
        error_exit("\nError: String argument must be non-empty.")

    start = 0
    while start < ls:
        end = start + 1
        while end <= ls:
            debug1("s[{}:{}] = {}".format(start, end, s[start:end]))
            yield s[start:end]
            end += 1
        start += 1

def main():
    if lsa != 2:
        usage()
        error_exit("\nError: Exactly one argument must be given.")

    for substring in all_substrings(sa[1]):
        print(substring)

sa = sys.argv
lsa = len(sa)

if __name__ == "__main__":
    main()

