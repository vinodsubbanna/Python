# 15)Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be: 11106
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

dig = input("Enter the digit :")
# dig2 = 11*dig
# dig3 = 111*dig
# dig4 = 1111*dig
# print(dig+dig2+dig3+dig4)

n1 = int("%s"% dig)
n2 = int("%s%s"%(dig,dig))
n3 = int("%s%s%s"%(dig,dig,dig))
n4 = int("%s%s%s%s"%(dig,dig,dig,dig))

print(n1+n2+n3+n4)