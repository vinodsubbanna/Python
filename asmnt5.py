# 5)Define a class which has at least two methods: getString: to get a
# string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class readString:
    def __init__(self):
        self.val = ""
    def getString(self):
        self.val=input("Enter the String : ")
    def printString(self):
        print ("String entered in Caps "+str(self.val.upper()))

strObj = readString()
strObj.getString()
strObj.printString()

