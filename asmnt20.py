# 20)Define a class with a generator which can iterate the numbers, which
# are divisible by 7, between a given range 0 and n.
# Hints:
# Consider use yield

class Generator:

    def __init__(self,n):
        self.n=n
    def gen(self):
        for i in range(1,self.n):
            if i %7==0:
                yield i


n = int(input("Enter the number :"))
munum = Generator(n)
result = munum.gen()
for num in result:
    print(num)

