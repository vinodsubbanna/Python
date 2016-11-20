#
# def palindrome(string):
#     text = "".join([e for e in string if e.isalpha()]).lower()
#     text2 = ""
#     for w in text[::-1]:
#         text2 += w
#
#     if text.__eq__(text2):
#         print("palindrome")
#     else:
#         print("Not palindrome")
#
# palindrome("Noel Sees Leon . ")

def squaretup():
    list = []
    for i in range(1,21):
        list.append(i**2)
    list = tuple(list)
    print(list)

squaretup()