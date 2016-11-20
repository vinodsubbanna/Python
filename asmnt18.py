# 18)A website requires the users to input username and password to
# register. Write a program to check the validity of password input by
# users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and
# will check them according to the above criteria. Passwords that match the
# criteria are to be printed, each separated by a comma.
import re
pwd = [x for x in input().split(",")]
val = []
for eachpwd in pwd:
    if len(eachpwd)<6 or len(eachpwd)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",eachpwd):
        continue
    elif not re.search("[0-9]",eachpwd):
        continue
    elif not re.search("[A-Z]",eachpwd):
        continue
    elif not re.search("[$#@]",eachpwd):
        continue
    else:
        pass
    val.append(eachpwd)
print(val)

# for eachpwd in pwd:
#     if re.match(r'[A-Za-z0-9$#@]{6,12}',eachpwd):
#         val.append(eachpwd)
#     else:
#         print("Not accepteed :"+str(eachpwd))
# print("Accepted Passwords :")
# print(" ".join(val))






