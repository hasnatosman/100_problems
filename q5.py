"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""


class InputOutString(object):

    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input('Input something you want to see: ')

    def get_print(self):
        print(self.s.upper())


objstr = InputOutString()
objstr.get_string()
objstr.get_print()
