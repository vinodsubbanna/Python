# 30)Define a function which can print a dictionary where the keys are
# numbers between 1 and 3 (both included) and the values are square of
# keys.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

def createDict(n):
    for i in range(n):
        dict[i]=int(i)**2
    print(dict)

dict={}
createDict(10)
