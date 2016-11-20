# 17)Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown
# as following:
# D 100
# W 200
# ¡
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be: 500
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

net_amount = 0
while True:
    line = input()
    if line:
        data = line.split(" ")
        trans = data[0]
        amount = int(data[1])
        if trans == 'D':
            net_amount = net_amount+amount
        elif trans == "W":
            net_amount = net_amount-amount
        else:
            pass
    else:
        break
print("Balance  :"+str(net_amount))






