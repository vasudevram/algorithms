
# debug1.py

# A simple debugging function for Python programs.
# If the built-in Python special variable __debug__ is not defined,
# the debug1 function does nothing.
# If the __debug__ variable is set to any value, the debug1 function 
# prints the message and all optional values passed to it.

from __future__ import print_function
import os

if __debug__:
    def debug1(message, *values):
        if len(values) == 0:
            print(message)
        else:
            print("{}:".format(message), end=" ")
            print(" ".join([repr(value) for value in values]))
else:
    def debug1(message, *values):
        pass

def main():
    # Test the debug1 function with some calls.
    debug1('message only')
    debug1('message with int', 1)
    debug1('message with int, float', 1, 2.3)
    debug1('message with long, string', 4L, "hi")
    debug1('message with boolean, tuple, set', True, (1, 2), { 3, 4} )
    debug1('message with string, boolean, list', "hi", True, [2, 3])
    debug1('message with complex, dict', 
        1 + 2j, {'a': 'apple', 'b': 'banana'})
    class Foo: pass
    foo = Foo()
    debug1('message with object', foo)
    debug1('message with class', Foo)
    debug1('message with xrange', xrange(3))
    debug1('message with listiterator', iter(range(4)))

if __name__ == '__main__':
    main()

