# 25)Define a class, which have a class parameter and have a same instance
# parameter.
# Hints:
# >Define a instance parameter, need add it in __init__ method You can init
# a object with construct parameter or set the value later
# >Define a function which can compute the sum of two numbers.
# Hints:
# Define a function with two numbers as arguments. You can compute the sum
# in the function and return the value.
# >Define a function that can convert a integer into a string and print it
# in console.
# Hints:
# Use str() to convert a number to string.
# >Define a function that can convert a integer into a string and print it
# in console.
# Hints:
# Use str() to convert a number to string.

class sample:
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b
    def sum(self):
        return self.a+self.b
    def cinIntToStr(self,inta):
        inta = str(inta)
        print(inta)
    def strToInt(self,stra):
        print(int(stra))

a1 = sample(2,9)
print(a1.sum())
a2 = "50"
a3 = 100
a1.cinIntToStr(a3)
a1.strToInt(a2)






