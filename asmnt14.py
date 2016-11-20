# 14)Write a program that accepts a sentence and calculate the number of
# upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1 LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

upp = 0
lowr = 0

data  = input("Enter the input data :")

for i in data:
    if i.isupper():
        upp = upp + 1
    elif i.islower():
        lowr = lowr +1
    else:
        pass

print("Upper "+str(upp))
print("Lower "+str(lowr))