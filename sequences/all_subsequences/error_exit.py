
# error_exit.py

# Purpose: This module, error_exit.py, defines a function with 
# the same name, error_exit(), which takes a string message 
# as an argument. It prints the message to sys.stderr, or 
# to another file object open for writing (if given as the 
# second argument), and then exits the program.
# The function error_exit can be used when a fatal error condition occurs, 
# and you therefore want to print an error message and exit your program.

import sys

def error_exit(message, dest=sys.stderr):
    dest.write(message)
    sys.exit(1)

def main():
    error_exit("Testing error_exit with dest sys.stderr (default).\n")
    error_exit("Testing error_exit with dest sys.stdout.\n", 
        sys.stdout)
    with open("temp1.txt", "w") as fil:
        error_exit("Testing error_exit with dest temp1.txt.\n", fil)

if __name__ == "__main__":
    main()


