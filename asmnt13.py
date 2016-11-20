# 13)Write a program that accepts a sentence and calculate the number of
# letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

let = 0
dig = 0

data = input("Enter the sentence : ")
for i in data:
    if i.isdigit():
        dig = dig+1
    elif i.isalpha():
        let = let + 1
    else :
        pass

print("Letter "+str(let))
print("Digits "+str(dig))

